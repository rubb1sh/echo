import unittest
import Filter
import re


class NamesTestCase(unittest.TestCase):
    def test_filter(self):
        self.assertEqual(True, Filter.Filter('简历12312', '简历', 'str'))

    def test_ff(self):
        s = '东北大学-牟俊树-后端开发'
        if Filter.minusSign(s) != True:
            print("%d\n", len(s))


if __name__ == "__main__":
    unittest.main()
