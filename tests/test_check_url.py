import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('check_url', Path(__file__).resolve().parents[1] / 'scripts/check_url.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CheckURLTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'resources'
        self.root.mkdir()

    def record(self, url):
        folder = self.root / 'R0001'
        folder.mkdir(exist_ok=True)
        (folder / 'README.md').write_text(f'# 测试文章\n\n- 原链接：{url}\n', encoding='utf-8')
        return folder

    def test_exact_only_uses_original_field(self):
        folder = self.record('https://example.com/Article')
        (folder / '正文.md').write_text('https://example.com/Other', encoding='utf-8')
        (self.root / 'README.md').write_text('https://example.com/Other', encoding='utf-8')
        self.assertEqual(module.check_url('https://example.com/Article', self.root)['status'], 'exact')
        self.assertEqual(module.check_url('https://example.com/Other', self.root)['status'], 'not_found')

    def test_tracking_is_only_possible_match(self):
        self.record('https://mp.weixin.qq.com/s/AbCd')
        self.assertEqual(module.check_url('https://mp.weixin.qq.com/s/AbCd?scene=21&utm_source=share#wechat_redirect', self.root)['status'], 'possible')

    def test_case_and_identity_parameters_are_preserved(self):
        self.record('https://mp.weixin.qq.com/s/AbCd?mid=1&sn=ABC')
        for url in ['https://mp.weixin.qq.com/s/abcd?mid=1&sn=ABC',
                    'https://mp.weixin.qq.com/s/AbCd?mid=2&sn=ABC',
                    'https://mp.weixin.qq.com/s/AbCd?mid=1&sn=abc']:
            with self.subTest(url=url):
                self.assertEqual(module.check_url(url, self.root)['status'], 'not_found')

    def test_meaningful_fragments_are_preserved(self):
        self.record('https://example.com/#/article/1')
        self.assertEqual(module.check_url('https://example.com/#/article/2', self.root)['status'], 'not_found')

    def test_invalid_record_prevents_false_clean_result(self):
        folder = self.record('https://example.com/Article')
        (folder / 'README.md').write_text('# 缺少链接', encoding='utf-8')
        self.assertEqual(module.check_url('https://example.com/new', self.root)['status'], 'error')

    def test_empty_library_and_missing_directory_differ(self):
        self.assertEqual(module.check_url('https://example.com/new', self.root)['status'], 'not_found')
        with self.assertRaises(ValueError):
            module.check_url('https://example.com/new', self.root / 'missing')

    def test_invalid_inputs(self):
        for url in ['not a url', 'file:///a', 'https://example.com:bad/a', 'https://example.com/a b']:
            with self.subTest(url=url), self.assertRaises(ValueError):
                module.check_url(url, self.root)


if __name__ == '__main__':
    unittest.main()
