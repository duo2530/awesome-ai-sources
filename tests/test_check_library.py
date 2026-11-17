import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/check_library.py'
spec = importlib.util.spec_from_file_location('check_library', SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write('README.md', '# 首页\n| 来源 | 1 篇 | [来源](sources/S0001.md) |\n')
        self.write('resources/R0001/README.md', '''# 示例文章
- 内容编号：R0001
- 原链接：https://example.com/article
- 发布来源：[来源](../../sources/S0001.md)
- 形式：文章
- 原文发布日期：2026-06-26
- 日期依据：用户提供
- 收录日期：2026-11-15
- 内容处理：已有正文与 AI 摘要
- 我的阅读：未记录

[正文](正文.md) · [标签](../../tags/知识.md) · [问题](../../problems/问题.md) · [作者](../../authors/A0001.md)
''')
        self.write('resources/R0001/正文.md', '# 原文\n<!-- 正文开始 -->\n' + '用户提供的第三方文字。' * 10 + '\n<!-- 正文结束 -->\n')
        self.write('resources/README.md', '''# 内容
| R0001 | [示例文章](R0001/README.md) | 一篇用于测试的示例文章摘要 | [来源](../sources/S0001.md) | 文章 | 已有正文与 AI 摘要 | 未记录 | 2026-06-26 |
''')
        self.write('sources/S0001.md', '# 来源\n## 已收录内容\n[资料](../resources/R0001/README.md)\n')
        self.write('sources/README.md', '# 来源\n| [来源](S0001.md) | 平台 | 1 篇 | 身份 |\n')
        self.write('authors/A0001.md', '# 作者\n[资料](../resources/R0001/README.md)\n')
        self.write('authors/README.md', '# 作者\n[作者](A0001.md)\n')
        self.write('tags/知识.md', '# 知识\n[资料](../resources/R0001/README.md)\n')
        self.write('tags/README.md', '# 标签\n[知识](知识.md)（1 条）\n')
        self.write('problems/问题.md', '# 问题\n[资料](../resources/R0001/README.md)\n')
        self.write('problems/README.md', '# 问题\n[问题](问题.md)\n')
        self.write('log.md', '# 日志\n## [2026-11-15] ingest | 示例\n')

    def write(self, name, text):
        file = self.root / name
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding='utf-8')

    def replace(self, name, old, new):
        file = self.root / name
        self.write(name, file.read_text(encoding='utf-8').replace(old, new))

    def check(self):
        return checker.check_library(self.root)

    def test_valid_library_is_read_only(self):
        before = {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(self.check()['errors'], [])
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_invalid_calendar_date_is_rejected(self):
        self.replace('resources/R0001/README.md', '2026-06-26', '2026-02-30')
        self.assertTrue(any('发布日期非法' in e for e in self.check()['errors']))

    def test_unknown_publication_date_is_warning(self):
        self.replace('resources/R0001/README.md', '2026-06-26', '待补充')
        self.replace('resources/README.md', '2026-06-26', '待补充')
        result = self.check()
        self.assertEqual(result['errors'], [])
        self.assertEqual(len(result['warnings']), 1)

    def test_status_and_empty_original_cannot_claim_processed(self):
        self.write('resources/R0001/正文.md', '# 示例\n<!-- 正文开始 -->\n\n<!-- 正文结束 -->')
        self.assertTrue(any('原始材料为空' in e for e in self.check()['errors']))
        self.replace('resources/R0001/README.md', '已有正文与 AI 摘要', '已经全部学会')
        self.assertTrue(any('状态不受支持' in e for e in self.check()['errors']))

    def test_missing_link_and_anchor_are_reported(self):
        self.write('WORKFLOW.md', '# 流程\n[不存在](missing.md)\n[错锚点](README.md#不存在)\n')
        errors = self.check()['errors']
        self.assertTrue(any('链接不存在' in e for e in errors))
        self.assertTrue(any('锚点不存在' in e for e in errors))

    def test_code_examples_and_third_party_links_are_excluded(self):
        self.write('WORKFLOW.md', '# 流程\n```markdown\n[示例](missing.md)\n```\n[外部](https://example.com/missing)\n')
        self.write('resources/R0001/正文.md', '第三方原文不要求内部链接可达。' * 10 + '\n[第三方相对路径](upstream.md)')
        self.assertEqual(self.check()['errors'], [])

    def test_reading_and_processing_index_drift_are_errors(self):
        self.replace('resources/README.md', '| 未记录 |', '| 已读 |')
        self.assertTrue(any('我的阅读与内容入口不一致' in e for e in self.check()['errors']))

    def test_missing_index_row_and_duplicate_row_are_errors(self):
        file = self.root / 'resources/README.md'
        text = file.read_text(encoding='utf-8')
        self.write('resources/README.md', text + text.splitlines()[1] + '\n')
        self.assertTrue(any('重复编号' in e for e in self.check()['errors']))
        self.write('resources/README.md', '# 内容\n')
        self.assertTrue(any('编号与正式资料目录不一致' in e for e in self.check()['errors']))

    def test_tag_count_and_reverse_links_are_checked(self):
        self.replace('tags/README.md', '（1 条）', '（2 条）')
        self.write('problems/问题.md', '# 问题\n')
        errors = self.check()['errors']
        self.assertTrue(any('数量应为 1' in e for e in errors))
        self.assertTrue(any('关联页缺少返回' in e for e in errors))

    def test_source_related_reading_is_not_source_membership(self):
        self.write('sources/S0002.md', '# 旧来源\n- 历史来源编号：S0002\n[当前](S0001.md)')
        text = '# 来源\n## 已收录内容\n[收录](first.md)\n## 关联发布入口\n[推荐](second.md)\n'
        self.assertEqual(checker.links(checker.section(text, '已收录内容')), ['first.md'])
        self.assertEqual(self.check()['errors'], [])
        self.replace('resources/R0001/README.md', 'S0001.md', 'S0002.md')
        self.assertTrue(any('历史归并页' in e for e in self.check()['errors']))

    def test_registered_source_without_articles_is_allowed(self):
        self.write('sources/S0002.md', '# 新来源\n## 已收录内容\n\n当前 0 篇。\n')
        self.replace('sources/README.md', '| 身份 |', '| 身份 |\n\n- [新来源](S0002.md)：0 篇')
        self.assertEqual(self.check()['errors'], [])
        self.replace('sources/README.md', '\n\n- [新来源](S0002.md)：0 篇', '')
        self.assertTrue(any('索引成员与正式页面不一致' in e for e in self.check()['errors']))

    def test_partial_dates_keep_their_original_precision(self):
        for value in ('2026', '2026-06'):
            with self.subTest(value=value):
                self.replace('resources/R0001/README.md', '2026-06-26', value)
                self.replace('resources/README.md', '2026-06-26', value)
                self.assertEqual(self.check()['errors'], [])
                self.replace('resources/R0001/README.md', f'原文发布日期：{value}\n', '原文发布日期：2026-06-26\n')
                self.replace('resources/README.md', f'| {value} |', '| 2026-06-26 |')

    def test_title_and_form_must_match_content_entry(self):
        self.replace('resources/README.md', '[示例文章]', '[错误标题]')
        self.replace('resources/README.md', '| 文章 |', '| 视频 |')
        errors = self.check()['errors']
        self.assertTrue(any('标题与内容入口不一致' in e for e in errors))
        self.assertTrue(any('形式与内容入口不一致' in e for e in errors))

    def test_table_broken_by_blank_line_is_reported(self):
        self.write('authors/README.md', '# 作者\n| 作者 | 背景 |\n|---|---|\n| [A](A0001.md) | x |\n\n| [A](A0001.md) | y |\n')
        self.assertTrue(any('表格被空行打断' in e for e in self.check()['errors']))

    def test_table_column_mismatch_is_reported(self):
        self.write('authors/README.md', '# 作者\n| 作者 | 背景 |\n|---|---|\n| [A](A0001.md) | x | 多余 |\n')
        self.assertTrue(any('列数与表头不一致' in e for e in self.check()['errors']))

    def test_unclosed_fence_and_comment_are_reported(self):
        self.write('WORKFLOW.md', '# 流程\n```text\n示例\n')
        self.assertTrue(any('围栏未闭合' in e for e in self.check()['errors']))
        self.write('WORKFLOW.md', '# 流程\n<!-- 未闭合\n')
        self.assertTrue(any('HTML 注释未闭合' in e for e in self.check()['errors']))

    def test_loose_list_and_single_pipe_paragraph_are_not_errors(self):
        self.write('WORKFLOW.md', '# 流程\n- 一\n\n- 二\n\n| 单行段落 |\n')
        self.assertEqual(self.check()['errors'], [])

    def test_cli_uses_script_root_and_reports_nonzero_on_errors(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '--root', str(self.root), '--json'],
                                cwd=self.temp.name, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.write('problems/问题.md', '# 问题\n[失效](missing.md)')
        result = subprocess.run([sys.executable, str(SCRIPT), '--root', str(self.root), '--json'],
                                cwd=self.temp.name, capture_output=True)
        self.assertEqual(result.returncode, 2)

    def test_index_summary_column_is_required(self):
        self.replace('resources/README.md', '一篇用于测试的示例文章摘要', '太短')
        self.assertTrue(any('一句话摘要应为 8–80 字' in e for e in self.check()['errors']))

    def test_entry_without_problem_page_is_warned(self):
        self.replace('resources/R0001/README.md', ' · [问题](../../problems/问题.md)', '')
        self.assertTrue(any('未被任何问题页引用' in w for w in self.check()['warnings']))

    def test_topic_page_checks(self):
        self.write('synthesis/README.md',
                   '# 综合\n| 编号 | 主题 | 涉及资料 | 最近修订 |\n|---|---|---|---|\n'
                   '| [T0001](T0001-示例.md) | 示例 | [R0001](../resources/R0001/README.md) | 2026-11-15 |\n')
        self.write('synthesis/T0001-示例.md', '''# 示例主题
- 综合编号：T0001
- 主题：示例
- 涉及资料：[R0001](../resources/R0001/README.md)
- 最近修订：2026-11-15
- 依据范围：示例
- 内容处理：已有 AI 综合
''')
        self.assertTrue(any('涉及资料须链接至少两条正式内容' in e for e in self.check()['errors']))
        self.replace('synthesis/T0001-示例.md', '综合编号：T0001', '综合编号：T0002')
        self.assertTrue(any('综合编号与文件名不一致' in e for e in self.check()['errors']))
        self.replace('synthesis/T0001-示例.md', '综合编号：T0002', '综合编号：T0001')
        self.replace('synthesis/README.md', '2026-11-15', '2026-11-14')
        self.assertTrue(any('最近修订与页面不一致' in e for e in self.check()['errors']))

    def test_topic_without_index_record_is_reported(self):
        self.write('synthesis/README.md', '# 综合\n| 编号 | 主题 | 涉及资料 | 最近修订 |\n|---|---|---|---|\n')
        self.write('synthesis/T0001-示例.md', '''# 示例主题
- 综合编号：T0001
- 主题：示例
- 涉及资料：[R0001](../resources/R0001/README.md)
- 最近修订：2026-11-15
- 依据范围：示例
- 内容处理：已有 AI 综合
''')
        self.assertTrue(any('缺少 T0001 的索引记录' in e for e in self.check()['errors']))

    def test_log_format_order_and_references_are_checked(self):
        self.replace('log.md', 'ingest', 'unknown')
        self.assertTrue(any('未知日志类型' in e for e in self.check()['errors']))
        self.write('log.md', '# 日志\n## [2026-11-15] ingest | 后\n## [2026-11-14] ingest | 前\n')
        self.assertTrue(any('时间正序' in e for e in self.check()['errors']))
        self.write('log.md', '# 日志\n## [2026-11-15] ingest | 引用 R9999\n')
        self.assertTrue(any('R9999 不存在' in e for e in self.check()['errors']))
        (self.root / 'log.md').unlink()
        self.assertTrue(any('缺少维护日志' in e for e in self.check()['errors']))


if __name__ == '__main__':
    unittest.main()
