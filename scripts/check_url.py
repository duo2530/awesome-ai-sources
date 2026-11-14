"""只读、本地 URL 查重。Markdown 内容入口是唯一数据来源，不联网。"""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


DEFAULT_RESOURCES = Path(__file__).resolve().parents[1] / 'resources'


def validate_url(url):
    parts = urlsplit(url)
    if (parts.scheme not in ('http', 'https') or not parts.hostname
            or re.search(r'\s', url) or parts.username or parts.password):
        raise ValueError('请提供完整的 http(s) 原链接，不要包含空格或账号密码。')
    _ = parts.port  # 验证端口是否合法。
    return parts


def comparison_key(url):
    """仅用于提示疑似重复，不作为自动合并依据。路径与参数大小写保留。"""
    parts = validate_url(url)
    host = parts.hostname.lower()
    port = parts.port
    netloc = f'[{host}]' if ':' in host else host
    if port and (parts.scheme, port) not in (('https', 443), ('http', 80)):
        netloc += f':{port}'
    ignored = {'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'utm_id'}
    if host == 'mp.weixin.qq.com':
        ignored |= {'scene', 'subscene', 'from', 'isappinstalled', 'clicktime', 'enterid'}
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
             if k.lower() not in ignored]
    fragment = parts.fragment
    if host == 'mp.weixin.qq.com' and fragment == 'wechat_redirect':
        fragment = ''
    return urlunsplit((parts.scheme, netloc, parts.path, urlencode(query), fragment))


def check_url(url, resources_dir=DEFAULT_RESOURCES):
    validate_url(url)
    resources_dir = Path(resources_dir)
    if not resources_dir.is_dir():
        raise ValueError(f'正式资料目录不存在：{resources_dir}')
    entries = sorted(p for p in resources_dir.glob('R*/README.md')
                     if re.fullmatch(r'R\d+', p.parent.name))
    matches = []
    errors = []
    key = comparison_key(url)
    for file in entries:
        text = file.read_text(encoding='utf-8-sig')
        links = re.findall(r'^- 原链接：\s*(\S+)\s*$', text, flags=re.M)
        if len(links) != 1:
            errors.append(f'{file}: 应有且仅有一个“- 原链接：”字段')
            continue
        original = links[0]
        try:
            record_key = comparison_key(original)
        except ValueError as exc:
            errors.append(f'{file}: {exc}')
            continue
        kind = 'exact' if original == url else 'possible' if record_key == key else None
        if kind:
            title = re.search(r'^# (.+)$', text, flags=re.M)
            matches.append(dict(kind=kind, id=file.parent.name,
                                title=title[1] if title else file.parent.name,
                                url=original, path=str(file.resolve())))
    status = ('error' if errors else 'exact' if any(m['kind'] == 'exact' for m in matches)
              else 'possible' if matches else 'not_found')
    return dict(status=status, checked=len(entries), matches=matches, errors=errors)


def main(argv=None):
    parser = argparse.ArgumentParser(description='只检查正式资料的原链接，不联网、不修改文件。')
    parser.add_argument('url', help='待收录的原链接；含 & 等字符时用引号包住')
    parser.add_argument('--json', action='store_true', help='输出 JSON，供 AI 或其他脚本读取')
    parser.add_argument('--resources-dir', type=Path, default=DEFAULT_RESOURCES,
                        help='正式资料目录，默认按脚本位置定位，与当前工作目录无关')
    args = parser.parse_args(argv)
    try:
        result = check_url(args.url.strip(), args.resources_dir)
    except (OSError, UnicodeError, ValueError) as exc:
        result = dict(status='error', checked=0, matches=[], errors=[str(exc)])
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        labels = {'exact': '已收录：链接完全一致', 'possible': '疑似重复：仅可识别的格式或追踪参数有差异，请核对',
                  'not_found': '未发现相同或疑似链接（不保证不存在其他形式的同一内容）',
                  'error': '检查未完整成功，请先处理错误，不能据此判定未收录'}
        print(labels[result['status']])
        print(f"已扫描 {result['checked']} 条正式记录；未访问网络。")
        for match in result['matches']:
            print(f"[{match['kind']}] {match['id']} · {match['title']}\n{match['path']}")
        for error in result['errors']:
            print(f'错误：{error}', file=sys.stderr)
    return {'not_found': 0, 'exact': 1, 'error': 2, 'possible': 3}[result['status']]


if __name__ == '__main__':
    raise SystemExit(main())
