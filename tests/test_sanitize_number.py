import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from json_transform import sanitize_number

class TestSanitizeNumber(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(sanitize_number(''))

    def test_whitespace_string(self):
        self.assertIsNone(sanitize_number('   '))

    def test_positive_integer(self):
        self.assertEqual(sanitize_number('  123  '), 123)

    def test_negative_integer(self):
        self.assertEqual(sanitize_number('  -456  '), -456)

    def test_positive_float(self):
        self.assertEqual(sanitize_number('  3.14  '), 3.14)

    def test_negative_float(self):
        self.assertEqual(sanitize_number('  -2.718  '), -2.718)

    def test_zero(self):
        self.assertEqual(sanitize_number('  0  '), 0)

    def test_invalid_number(self):
        self.assertIsNone(sanitize_number('  abc  '))


if __name__ == '__main__':
    unittest.main()