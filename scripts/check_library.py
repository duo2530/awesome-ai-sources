"""只读检查正式 Markdown 资料；不联网、不修复、不扫描第三方正文。"""
import argparse
from collections import Counter
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+"[^"\n]*")?\s*\)')


def without_code(text):
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            lines.append('')
        else:
            lines.append('' if fence else line)
    return '\n'.join(lines)


def links(text):
    return [m[1].strip('<>') for m in LINK.finditer(without_code(text))]


def fields(text):
    return dict(re.findall(r'^- ([^：\n]+)：([^\n]*)$', text, re.M))


def section(text, title):
    match = re.search(r'^## ' + re.escape(title) + r'\s*\n(.*?)(?=^## |\Z)', text, re.M | re.S)
    return match[1] if match else ''


FENCE = re.compile(r'^\s*(`{3,}|~{3,})')


def table_cells(line):
    """按未转义竖线切分表格行，忽略首尾边界竖线。"""
    parts = re.split(r'(?<!\\)\|', line.strip())
    if parts and not parts[0].strip():
        parts = parts[1:]
    if parts and not parts[-1].strip():
        parts = parts[:-1]
    return parts


def block_errors(text):
    """检查维护文件的块结构；不得传入第三方原始正文。

    只覆盖可机械判定的渲染缺陷：围栏与注释是否闭合、表格是否被空行打断、
    表格列数与表头是否一致。单个以竖线开头的段落不视为表格，列表间的空行
    属合法的松散列表，均不报错。
    """
    messages = []
    if sum(1 for line in text.splitlines() if FENCE.match(line)) % 2:
        messages.append('代码围栏未闭合（围栏标记数为奇数）')
    plain = without_code(text)
    if plain.count('<!--') != plain.count('-->'):
        messages.append('HTML 注释未闭合（起止标记数量不一致）')
    lines = plain.splitlines()
    for index in range(1, len(lines) - 1):
        if not lines[index].strip() and lines[index - 1].startswith('|') and lines[index + 1].startswith('|'):
            messages.append(f'第 {index + 1} 行：表格被空行打断')
    index = 0
    while index < len(lines):
        if not lines[index].startswith('|'):
            index += 1
            continue
        start = index
        block = []
        while index < len(lines) and lines[index].startswith('|'):
            block.append((index, lines[index]))
            index += 1
        if len(block) < 2:
            continue
        delimiter = block[1][1]
        if not re.fullmatch(r'[\s|:\-]+', delimiter) or '-' not in delimiter:
            messages.append(f'第 {start + 1} 行：连续的表格行缺少分隔行')
            continue
        width = len(table_cells(block[0][1]))
        for row, line in block:
            count = len(table_cells(line))
            if width and count != width:
                messages.append(f'第 {row + 1} 行：表格列数与表头不一致（{count} 列，应为 {width} 列）')
    return messages


def local_target(file, url):
    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        return None
    return (file.parent / unquote(parts.path)).resolve() if parts.path else file.resolve()


def heading_ids(text):
    result, seen = set(), Counter()
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', without_code(text), re.M):
        title = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', title)
        slug = re.sub(r'[^\w\-\s]', '', title.lower()).replace(' ', '-')
        number = seen[slug]
        seen[slug] += 1
        result.add(slug if not number else f'{slug}-{number}')
    return result


def check_library(root=ROOT):
    root = Path(root).resolve()
    errors, warnings, texts = [], [], {}

    def error(file, message):
        errors.append(f'{file.relative_to(root)}: {message}')

    required = ['README.md', 'resources/README.md', 'sources/README.md',
                'authors/README.md', 'tags/README.md', 'problems/README.md']
    files = {root / name for name in required}
    files.update(root / name for name in ('AGENTS.md', 'WORKFLOW.md') if (root / name).exists())
    if (root / 'log.md').is_file():
        files.add(root / 'log.md')
    for directory in ('sources', 'authors', 'tags', 'problems', 'synthesis'):
        files.update((root / directory).glob('*.md'))
    entries = sorted(p for p in (root / 'resources').glob('R*/README.md')
                     if re.fullmatch(r'R\d+', p.parent.name))
    topics = sorted(p for p in (root / 'synthesis').glob('T*.md')
                    if re.fullmatch(r'T\d+-.+\.md', p.name))
    files.update(entries)
    files.update(topics)
    for file in sorted(files):
        try:
            texts[file.resolve()] = file.read_text(encoding='utf-8-sig')
        except (OSError, UnicodeError) as exc:
            error(file, f'无法读取：{exc}')

    def targets(file, text):
        result = set()
        for link in links(text):
            try:
                target = local_target(file, link)
            except ValueError as exc:
                error(file, f'链接格式错误 {link}：{exc}')
                continue
            if target is not None:
                result.add(target)
        return result

    for file, text in texts.items():
        for message in block_errors(text):
            error(file, message)

    references = {file: targets(file, text) for file, text in texts.items()}
    for file, text in texts.items():
        for link in links(text):
            try:
                target = local_target(file, link)
                fragment = unquote(urlsplit(link).fragment)
            except ValueError:
                continue
            if target is None:
                continue
            if not target.is_relative_to(root):
                error(file, f'内部链接越出资料库：{link}')
            elif not target.exists():
                error(file, f'内部链接不存在：{link}')
            elif fragment and target in texts and fragment not in heading_ids(texts[target]):
                error(file, f'章节锚点不存在：{link}')

    metadata, source_members, tag_members = {}, {}, {}
    problem_members = set()
    for file in entries:
        file = file.resolve()
        text = texts.get(file, '')
        meta = fields(text)
        metadata[file] = meta
        for key in ('内容编号', '原链接', '发布来源', '形式', '原文发布日期',
                    '日期依据', '收录日期', '内容处理', '我的阅读'):
            occurrences = re.findall(r'^- ' + re.escape(key) + r'：([^\n]*)$', text, re.M)
            if len(occurrences) != 1 or not occurrences[0].strip():
                error(file, f'字段“{key}”必须唯一且非空')
        if meta.get('内容编号') != file.parent.name:
            error(file, '内容编号与目录不一致')
        repo = '代码仓库' in meta.get('形式', '')
        status = meta.get('内容处理', '')
        waiting = status.startswith('链接已收录，')
        if repo:
            if not (status == '链接已收录，仓库待阅读' or status.startswith(('已读', '已实践'))):
                error(file, '代码仓库的内容处理状态不受支持')
            if not meta.get('原文发布日期', '').startswith('不适用（'):
                error(file, '代码仓库不能填写文章发布日期')
        else:
            if meta.get('原文发布日期', '').startswith('不适用'):
                error(file, '文章须填写发布日期或待补充，不能写不适用')
            if not (status == '链接已收录，正文待提供' or (status.startswith('已有') and '摘要' in status)):
                error(file, '文章的内容处理状态不受支持')
            original = file.parent / '正文.md'
            if not original.is_file():
                error(file, '文章缺少正文.md（待提供也应有正文入口）')
            elif not waiting:
                try:
                    body = original.read_text(encoding='utf-8-sig')
                    if '<!-- 正文开始 -->' in body:
                        body = body.split('<!-- 正文开始 -->', 1)[1].split('<!-- 正文结束 -->', 1)[0]
                    if len(body.strip()) < 40:
                        error(file, '处理状态称已整理，但原始材料为空或过短，请人工核对')
                except (OSError, UnicodeError) as exc:
                    error(file, f'正文无法读取：{exc}')
        for key, value in meta.items():
            if '日期' not in key and key not in ('仓库创建时间', '最近阅读时间'):
                continue
            if key == '日期依据':
                continue
            if value.startswith(('待补充', '待核验', '未核验', '未记录', '不适用', '无')):
                if key == '原文发布日期' and not repo:
                    warnings.append(f'{file.relative_to(root)}: 发布日期待补充')
                continue
            match = re.match(r'^(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?(?=$|\s|（|\()', value)
            try:
                if not match:
                    raise ValueError('应使用 YYYY、YYYY-MM 或 YYYY-MM-DD，或明确标注待核验')
                year, month, day = match.groups()
                date(int(year), int(month or 1), int(day or 1))
            except ValueError as exc:
                error(file, f'{key}非法：{value}（{exc}）')
        source_refs = targets(file, meta.get('发布来源', ''))
        if len(source_refs) != 1:
            error(file, '发布来源须链接到一个正式来源页')
        for source in source_refs:
            if source.parent != root / 'sources' or not re.fullmatch(r'S\d+\.md', source.name):
                error(file, '发布来源不是正式来源编号页')
            if '历史来源编号' in texts.get(source, ''):
                error(file, '发布来源仍指向历史归并页')
            source_members.setdefault(source, set()).add(file)
        for target in references.get(file, set()):
            if target.parent == root / 'tags' and target.name != 'README.md':
                tag_members.setdefault(target, set()).add(file)
            if target.parent == root / 'problems' and target.name != 'README.md':
                problem_members.add(file)
            if target.parent in (root / 'tags', root / 'problems', root / 'authors') and target.name != 'README.md':
                if file not in references.get(target, set()):
                    error(file, f'关联页缺少返回本资料的链接：{target.relative_to(root)}')
        for source in source_refs:
            if file not in references.get(source, set()):
                error(file, f'来源页漏收录本资料：{source.name}')

    entry_set = set(metadata)
    tagged = set().union(*tag_members.values()) if tag_members else set()
    for file in sorted(entry_set - tagged):
        warnings.append(f'{file.relative_to(root)}: 未被任何标签页引用')
    for file in sorted(entry_set - problem_members):
        warnings.append(f'{file.relative_to(root)}: 未被任何问题页引用')
    index = root / 'resources/README.md'
    rows = {}
    for line in texts.get(index, '').splitlines():
        match = re.match(r'^\| (R\d+) \|', line)
        if match:
            # 标题可能含全角｜；半角分隔符须按 Markdown 表格转义。
            cells = re.split(r'(?<!\\)\|', line)[1:-1]
            if match[1] in rows:
                error(index, f'重复编号 {match[1]}')
            rows[match[1]] = [c.strip() for c in cells]
    if set(rows) != {p.parent.name for p in entry_set}:
        error(index, '全部内容表格编号与正式资料目录不一致')
    for file, meta in metadata.items():
        cells = rows.get(file.parent.name, [])
        if len(cells) != 8:
            error(index, f'{file.parent.name} 应有八列表格记录')
            continue
        if file not in targets(index, cells[1]):
            error(index, f'{file.parent.name} 标题链接指向错误')
        title = re.search(r'^# (.+)$', texts.get(file, ''), re.M)
        index_title = re.match(r'^\[([^\]]+)\]\(', cells[1])
        if title and (not index_title or index_title[1] != title[1]):
            error(index, f'{file.parent.name} 的标题与内容入口不一致')
        summary = cells[2]
        if not 8 <= len(summary) <= 80:
            error(index, f'{file.parent.name} 的一句话摘要应为 8–80 字')
        for column, key in ((4, '形式'), (5, '内容处理'), (6, '我的阅读')):
            if cells[column] != meta.get(key):
                error(index, f'{file.parent.name} 的{key}与内容入口不一致')
        date_value = meta.get('原文发布日期', '')
        expected = ('不适用（仓库）' if '代码仓库' in meta.get('形式', '') else
                    '待补充' if date_value.startswith('待补充') else date_value.split('（')[0].split(' ')[0])
        if cells[7] != expected:
            error(index, f'{file.parent.name} 的发布日期与内容入口不一致')
        if targets(index, cells[3]) != targets(file, meta.get('发布来源', '')):
            error(index, f'{file.parent.name} 的来源与内容入口不一致')

    topic_index = root / 'synthesis/README.md'
    if topic_index.exists() or topics:
        if topic_index not in texts:
            error(topic_index, '综合索引缺失或无法读取')
        rows, ids = {}, set()
        for line in texts.get(topic_index, '').splitlines():
            match = re.match(r'^\|\s*\[(T\d+)\]\(([^)]+)\)\s*\|', line)
            if not match:
                continue
            if match[1] in rows:
                error(topic_index, f'重复综合编号 {match[1]}')
            rows[match[1]] = (match[2], [c.strip() for c in table_cells(line)])
        for file in topics:
            file = file.resolve()
            text = texts.get(file, '')
            meta = fields(text)
            topic_id = file.name.split('-', 1)[0]
            ids.add(topic_id)
            for key in ('综合编号', '主题', '涉及资料', '最近修订', '依据范围', '内容处理'):
                occurrences = re.findall(r'^- ' + re.escape(key) + r'：([^\n]*)$', text, re.M)
                if len(occurrences) != 1 or not occurrences[0].strip():
                    error(file, f'字段“{key}”必须唯一且非空')
            if meta.get('综合编号') != topic_id:
                error(file, '综合编号与文件名不一致')
            if len(targets(file, meta.get('涉及资料', '')) & entry_set) < 2:
                error(file, '涉及资料须链接至少两条正式内容')
            value = meta.get('最近修订', '')
            try:
                match = re.match(r'^(\d{4})-(\d{2})-(\d{2})(?=$|\s|（|\()', value)
                if not match:
                    raise ValueError('应使用 YYYY-MM-DD')
                date(int(match[1]), int(match[2]), int(match[3]))
            except ValueError as exc:
                error(file, f'最近修订非法：{value}（{exc}）')
            row = rows.get(topic_id)
            if not row:
                error(topic_index, f'缺少 {topic_id} 的索引记录')
                continue
            if not row[0].startswith(('http://', 'https://')):
                if (topic_index.parent / unquote(row[0])).resolve() != file:
                    error(topic_index, f'{topic_id} 的链接指向错误')
            if row[1] and row[1][-1] != meta.get('最近修订', ''):
                error(topic_index, f'{topic_id} 的最近修订与页面不一致')
        for topic_id in sorted(set(rows) - ids):
            error(topic_index, f'索引中的 {topic_id} 没有对应页面')

    log = root / 'log.md'
    if not log.is_file():
        error(log, '缺少维护日志 log.md')
    else:
        logged = []
        for line in texts.get(log, '').splitlines():
            if not line.startswith('## '):
                continue
            match = re.match(r'^## \[(\d{4}-\d{2}-\d{2})\] (\S+) \| (.+)$', line)
            if not match:
                error(log, f'日志条目格式不符：{line[:40]}')
                continue
            logged.append(match)
        if not logged:
            error(log, '日志至少应有一条记录')
        previous = None
        for match in logged:
            try:
                day = date(int(match[1][:4]), int(match[1][5:7]), int(match[1][8:10]))
            except ValueError:
                error(log, f'日志日期非法：{match[1]}')
                continue
            if match[2] not in ('ingest', 'query', 'lint', 'synthesis', 'schema'):
                error(log, f'未知日志类型：{match[2]}')
            if previous and day < previous:
                error(log, '日志须按时间正序追加')
            previous = day
            for record in re.findall(r'R\d+', match[3]):
                if not (root / 'resources' / record).is_dir():
                    error(log, f'日志引用的 {record} 不存在')

    def check_members(index_file, members, directory):
        actual = {p for p in (root / directory).glob('*.md') if p.name != 'README.md'}
        if directory == 'sources':
            actual = {p for p in actual if '历史来源编号' not in texts.get(p, '')}
        if actual != set(members):
            error(index_file, f'{directory} 存在未关联资料的页面，或正式页面缺失')
        indexed = {p for p in references.get(index_file, set()) if p.parent == root / directory and p.name != 'README.md'}
        if indexed != actual:
            error(index_file, f'{directory} 索引成员与正式页面不一致（历史归并页不计入）')
        for page, expected_members in members.items():
            found = (targets(page, section(texts.get(page, ''), '已收录内容'))
                     if directory == 'sources' else references.get(page, set())) & entry_set
            if found != expected_members:
                error(page, '资料列表与内容入口关联不一致')

    check_members(root / 'tags/README.md', tag_members, 'tags')
    check_members(root / 'sources/README.md', source_members, 'sources')
    tag_index = root / 'tags/README.md'
    for tag, members in tag_members.items():
        pattern = re.escape(f']({tag.name})（{len(members)} 条）')
        if not re.search(pattern, texts.get(tag_index, '')):
            error(tag_index, f'{tag.stem} 的数量应为 {len(members)}')
    for directory in ('authors', 'problems'):
        idx = root / directory / 'README.md'
        actual = {p for p in (root / directory).glob('*.md') if p.name != 'README.md'}
        indexed = {p for p in references.get(idx, set()) if p.parent == root / directory and p.name != 'README.md'}
        if actual != indexed:
            error(idx, '索引成员与正式页面不一致')
    for idx in (root / 'README.md', root / 'sources/README.md'):
        for source, members in source_members.items():
            row = next((line for line in texts.get(idx, '').splitlines()
                        if source in targets(idx, line) and line.startswith('|')), '')
            if not re.search(r'\|\s*' + str(len(members)) + r'\s*(?:篇|条|个)', row):
                error(idx, f'{source.stem} 的来源数量应为 {len(members)}')
    return dict(status='error' if errors else 'ok', checked=len(entries),
                errors=sorted(set(errors)), warnings=sorted(set(warnings)))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    try:
        result = check_library(args.root)
    except (OSError, UnicodeError, ValueError) as exc:
        result = dict(status='error', checked=0, errors=[str(exc)], warnings=[])
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"资料检查：{result['status']}；{result['checked']} 条；{len(result['errors'])} 个错误；{len(result['warnings'])} 个提醒。")
        for kind, label in (('errors', '错误'), ('warnings', '提醒')):
            for message in result[kind]:
                print(f'{label}：{message}')
    return 2 if result['errors'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
