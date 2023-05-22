import unittest
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from json_transform import transform_json

class TestTransformJson(unittest.TestCase):
    def test_empty_json(self):
        input_json = {}
        expected_output = {}
        self.assertEqual(transform_json(input_json), expected_output)

    def test_simple_json(self):
        input_json = {
            "number_1": {
                "N": "1.50"
            },
            "string_1": {
                "S": "784498"
            },
            "string_2": {
                "S": "2014-07-16T20:55:46Z"
            }
        }
        expected_output = {
            "number_1": {"N":1.5},
            "string_1": {"S":"784498"},
            "string_2": {"S":"1405558546.0"}
        }
        self.assertEqual(transform_json(input_json), expected_output)

    def test_nested_json(self):
        input_json = {
            "map_1": {
                "M": {
                    "bool_1": {
                        "BOOL": "truthy"
                    },
                    "null_1": {
                        "NULL": "true"
                    },
                    "list_1": {
                        "L": [
                            {"S": ""},
                            {"N": "011"},
                            {"N": "5215s"},
                            {"BOOL": "f"},
                            {"NULL": "0"}
                        ]
                    }
                }
            },
            "list_2": {
                "L": "noop"
            },
            "list_3": {
                "L": ["noop"]
            },
            "": {
                "S": "noop"
            }
        }
        expected_output = {
            "map_1": 
            {"M": {
                "null_1": {"NULL": "null"}, 
                "list_1": 
                    {"L": [
                        {"N": 11}, 
                        {"BOOL": False}]
                        }
                    }
                }
            }
        self.assertEqual(transform_json(input_json), expected_output)

    # Add more test cases for other variations of the JSON structure

if __name__ == '__main__':
    unittest.main()
