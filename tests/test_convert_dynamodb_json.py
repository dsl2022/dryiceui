import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from json_transform import convert_dynamodb_json

class TestConvertDynamoDBJson(unittest.TestCase):
    def test_convert_dynamodb_json_single_value(self):
        # Test a single value
        data = {
            "N": "42"
        }
        expected_result = "42"
        self.assertEqual(convert_dynamodb_json(data), expected_result)

        data = {
            "S": "Hello, World!"
        }
        expected_result = "Hello, World!"
        self.assertEqual(convert_dynamodb_json(data), expected_result)

        data = {
            "BOOL": "true"
        }
        expected_result = "true"
        self.assertEqual(convert_dynamodb_json(data), expected_result)

        data = {
            "NULL": "true"
        }
        expected_result = "true"
        self.assertEqual(convert_dynamodb_json(data), expected_result)

    def test_convert_dynamodb_json_map(self):
        # Test a map
        data = {
            "M": {
                "key1": {
                    "N": "42"
                },
                "key2": {
                    "S": "Hello, World!"
                }
            }
        }
        expected_result = {
            "key1": "42",
            "key2": "Hello, World!"
        }
        self.assertEqual(convert_dynamodb_json(data), expected_result)

    def test_convert_dynamodb_json_list(self):
        # Test a list
        data = {
            "L": [
                {
                    "N": "42"
                },
                {
                    "S": "Hello, World!"
                }
            ]
        }
        expected_result = [
            "42",
            "Hello, World!"
        ]
        self.assertEqual(convert_dynamodb_json(data), expected_result)

    def test_convert_dynamodb_json_nested(self):
        # Test nested structures
        data = {
            "M": {
                "key1": {
                    "L": [
                        {
                            "N": "42"
                        },
                        {
                            "S": "Hello, World!"
                        }
                    ]
                },
                "key2": {
                    "M": {
                        "subkey": {
                            "S": "Nested value"
                        }
                    }
                }
            }
        }
        expected_result = {
            "key1": [
                "42",
                "Hello, World!"
            ],
            "key2": {
                "subkey": "Nested value"
            }
        }
        self.assertEqual(convert_dynamodb_json(data), expected_result)

    def test_convert_dynamodb_json_invalid(self):
        # Test invalid input
        data = "invalid"
        expected_result = "invalid"
        self.assertEqual(convert_dynamodb_json(data), expected_result)

        data = None
        expected_result = None
        self.assertEqual(convert_dynamodb_json(data), expected_result)

if __name__ == '__main__':
    unittest.main()
