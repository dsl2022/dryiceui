import datetime
import json
import re
from datetime import datetime
import time
start_time = time.time()
file_path = 'data.json'
rfc3339_pattern= r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})(?:[+-]\d{2}:\d{2})?$'

# Open the file and load the JSON data
with open(file_path) as file:
    json_data = json.load(file)

def sanitize_key(key):
    return key.strip()

def sanitize_string(value):
    if not isinstance(value, str):
        value = str(value) 
    value = value.strip()
    if not value:
        return None
    # Check if the value is in RFC3339 format using regular expressions
    elif re.match(rfc3339_pattern, value):
        try:            
            datetime_object = datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
            # Convert datetime object to Unix Epoch (numeric data type)
            return str(datetime_object.timestamp())
        except ValueError:
            # If the value is not in the expected format, return the sanitized string
            return value
    else:
        # If the value is not in RFC3339 format, return the sanitized string        
        return value


def sanitize_boolean(value):
    value = value.strip().lower()
    if value in ['1', 't', 'true']:
        return True
    if value in ['0', 'f', 'false']:
        return False
    return None

def sanitize_number(value):       
    value = str(value).strip()
    if value == '0':
        return 0     
    value.lstrip('0') 
    if value:
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                pass
        
    return None

def sanitize_null(value):
    if value and value.strip().lower() in ['1', 't', 'true']:
        return "null"  # Null value
    else:
        return None  # Omit the field for non-null value or invalid value


def transform_value(value, data_type):
    if data_type == 'S':
        return sanitize_string(value)
    elif data_type == 'N':
        return sanitize_number(value)
    elif data_type == 'BOOL':
        return sanitize_boolean(value)
    elif data_type == 'NULL':
        return sanitize_null(value)
    else:
        return None  # Unsupported data type

def convert_dynamodb_json(data):
    if isinstance(data, dict):
        if len(data) == 1:
            data_type, value = next(iter(data.items()))
            if data_type in ["N", "S", "BOOL", "NULL"]:
                return value
            elif data_type == "M":
                return convert_dynamodb_json(value)
            elif data_type == "L":
                return [convert_dynamodb_json(item) for item in value]
        return {key: convert_dynamodb_json(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_dynamodb_json(item) for item in data]
    else:
        
        return data

def transform_json(data):
    transformed_data = {}
    if isinstance(data, dict):
        for key, value in data.items():
            sanitized_key = sanitize_key(key)
            if sanitized_key:
                if isinstance(value, dict):
                    transformed_values = transform_json(value)
                    if transformed_values:                        
                        transformed_data[sanitized_key] = transformed_values
                elif isinstance(value, list):
                    transformed_list = []                    
                    for item in value:
                        transformed_item = transform_json(item)
                        if transformed_item:
                            transformed_list.append(transformed_item)
                    if transformed_list:
                        transformed_data[sanitized_key] = transformed_list
                else:                    
                    transformed_value = transform_value(value, sanitized_key)
                    
                    if transformed_value is not None:                        
                        transformed_data[sanitized_key] = transformed_value
    return transformed_data


if __name__ == '__main__':
    # Transform the JSON data
    transformed_json = transform_json(json_data)
    transformed_json = convert_dynamodb_json(transformed_json)
    # Print the transformed JSON
    print(json.dumps(transformed_json, indent=2))
    print("--- %s seconds ---" % (time.time() - start_time))