# Code Challenge JSON Transformer

## Introduction

This script processes JSON data from a file and performs transformations based on specified rules. It includes the following functionalities:

- Opening and loading JSON data from a file specified by file_path.
- Sanitizing keys by removing leading and trailing whitespace.
- Sanitizing string values by removing leading and trailing whitespace.
- Handling specific data types such as numbers, booleans, and null values.
- Transforming the JSON data by applying the sanitization rules recursively to nested dictionaries and lists.
- Converting the DynamoDB JSON into regular JSON format.

- To run the script, make sure to provide the correct file path for the JSON data in the file_path variable. After executing the script, it will load and transform the JSON data, and then print the transformed JSON.

The execution time of the script is also measured and displayed using the time.time() function to provide an indication of the script's performance.

Please note that the script assumes the JSON data in the file is correctly formatted and matches the expected structure.

## Execution

To run the app use the following

```
python json_transform.py
```

## Unit tests

This project was developed with the TDD methodology in mind. All the unit tests for all utility functions exists in different test module files. And the script in `test_all.py` file loads all these modules and run them. Verbose mode is enable for giving full test result information.

To run all unit tests, run the following

```
python tests/test_all.py
```
