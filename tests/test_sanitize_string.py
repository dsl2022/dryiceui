import unittest
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from json_transform import sanitize_string

class TestSanitizeString(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(sanitize_string(''))

    def test_whitespace_string(self):
        self.assertIsNone(sanitize_string('   '))

    def test_non_rfc3339_string(self):
        self.assertEqual(sanitize_string('   Hello, World!   '), 'Hello, World!')

    def test_rfc3339_string(self):
        rfc3339_string = "2014-07-16T20:55:46Z"
        expected_timestamp = str(datetime.strptime(rfc3339_string, '%Y-%m-%dT%H:%M:%SZ').timestamp())
        self.assertAlmostEqual(sanitize_string(rfc3339_string), expected_timestamp)
    def test_non_string_input(self):
        non_string_value = 42
        expected_result = str(non_string_value).strip()
        self.assertEqual(sanitize_string(non_string_value), expected_result)

if __name__ == '__main__':
    unittest.main()