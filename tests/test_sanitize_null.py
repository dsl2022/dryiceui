import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from json_transform import sanitize_null

class TestSanitizeNull(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(sanitize_null(''))

    def test_whitespace_string(self):
        self.assertIsNone(sanitize_null('   '))

    def test_true_values(self):
        true_values = ['1', 't', 'T', 'true', 'True', 'TRUE']
        for value in true_values:
            self.assertTrue(sanitize_null(value))

    def test_false_values(self):
        false_values = ['0', 'f', 'F', 'false', 'False', 'FALSE']
        for value in false_values:
            self.assertIsNone(sanitize_null(value))

    def test_invalid_values(self):
        invalid_values = ['abc', 'yes', 'no', 'on', 'off']
        for value in invalid_values:
            self.assertIsNone(sanitize_null(value))

if __name__ == '__main__':
    unittest.main()
