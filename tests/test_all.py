import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.test_sanitize_string import TestSanitizeString
from tests.test_sanitize_number import TestSanitizeNumber
from tests.test_sanitize_boolean import TestSanitizeBoolean
from tests.test_sanitize_null import TestSanitizeNull
from tests.test_transform_json import TestTransformJson
from tests.test_convert_dynamodb_json import TestConvertDynamoDBJson
if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestSanitizeString))
    suite.addTests(loader.loadTestsFromTestCase(TestSanitizeNumber))
    suite.addTests(loader.loadTestsFromTestCase(TestSanitizeBoolean))
    suite.addTests(loader.loadTestsFromTestCase(TestSanitizeNull))
    suite.addTests(loader.loadTestsFromTestCase(TestTransformJson))
    suite.addTests(loader.loadTestsFromTestCase(TestConvertDynamoDBJson))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
