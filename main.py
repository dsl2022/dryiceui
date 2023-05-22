import json
import datetime

def transform_input(input_data):
    output = []
    
    # Transform map_1
    if 'map_1' in input_data:
        map_1 = input_data['map_1'].get('M', {})
        
        # Transform bool_1
        if 'bool_1' in map_1:
            bool_1 = map_1['bool_1'].get('BOOL', '').strip().lower()
            if bool_1 in ['1', 't', 'true']:
                map_1['bool_1'] = True
            elif bool_1 in ['0', 'f', 'false']:
                map_1['bool_1'] = False
            else:
                del map_1['bool_1']
        
        # Transform null_1
        if 'null_1' in map_1:
            null_1 = map_1['null_1'].get('NULL', '').strip().lower()
            if null_1 in ['1', 't', 'true']:
                map_1['null_1'] = None
            else:
                del map_1['null_1']
        
        # Transform list_1
        if 'list_1' in map_1:
            list_1 = map_1['list_1'].get('L', [])
            sanitized_list = []
            for item in list_1:
                if 'S' in item:
                    string_value = item['S'].strip()
                    if string_value:
                        sanitized_list.append(string_value)
                elif 'N' in item:
                    number_value = item['N'].strip().lstrip('0')
                    if number_value and number_value.isdigit():
                        sanitized_list.append(int(number_value))
                elif 'BOOL' in item:
                    bool_value = item['BOOL'].strip().lower()
                    if bool_value in ['1', 't', 'true']:
                        sanitized_list.append(True)
                    elif bool_value in ['0', 'f', 'false']:
                        sanitized_list.append(False)
                elif 'NULL' in item:
                    null_value = item['NULL'].strip().lower()
                    if null_value in ['1', 't', 'true']:
                        sanitized_list.append(None)
            if sanitized_list:
                map_1['list_1'] = sanitized_list
            else:
                del map_1['list_1']
        
        if map_1:
            output.append({'map_1': map_1})
    
    # Transform number_1
    if 'number_1' in input_data:
        number_1 = input_data['number_1'].get('N', '').strip().lstrip('0')
        if number_1 and number_1.replace('.', '').isdigit():
            output.append({'number_1': float(number_1)})
    
    # Transform string_1
    if 'string_1' in input_data:
        string_1 = input_data['string_1'].get('S', '').strip()
        if string_1:
            output.append({'string_1': string_1})
    
    # Transform string_2
    if 'string_2' in input_data:
        string_2 = input_data['string_2'].get('S', '').strip()
        if string_2:
            try:
                dt = datetime.datetime.strptime(string_2, '%Y-%m-%dT%H:%M:%SZ')
                unix_timestamp = int(dt.timestamp())
                output.append({'string_2': unix_timestamp})
            except ValueError:
                pass
    
    return output
input_json2 = '''{
  key:{
    "N":"1.50"
  }
}'''

# Sample Input
input_json = '''
{
  "number_1": {
    "N": "1.50"
  },
  "string_1": {
    "S": "784498 "
  },
  "string_2": {
    "S": "2014-07-16T20:55:46Z"
  },
  "map_1": {
    "M": {
      "bool_1": {
        "BOOL": "truthy"
      },
      "null_1": {
        "NULL ": "true"
      },
      "list_1": {
        "L": [
          {
            "S": ""
          },
          {
            "N": "011"
          },
          {
            "N": "5215s"
          },
          {
            "BOOL": "f"
          },
          {
            "NULL": "0"
          }
        ]
      }
    }
  },
  "list_2": {
    "L": [
          {
            "S": ""
          },
          {
            "N": "011"
          },
          {
            "N": "5215s"
          },
          {
            "BOOL": "f"
          },
          {
            "NULL": "0"
          }
        ]
  },
  "list_3": {
    "L": [
      "noop"
    ]
  },
  "": {
    "S": "noop"
  }
}
'''

def sanitize_string(value):
    return value.strip()

def sanitize_number(value):
    value = value.strip().lstrip('0')
    if value and value.replace('.', '').isdigit():
        return float(value)
    return None

def sanitize_boolean(value):
    value = value.strip().lower()
    if value in ['1', 't', 'true']:
        return True
    if value in ['0', 'f', 'false']:
        return False
    return None

def sanitize_null(value):
    value = value.strip().lower()
    if value in ['1', 't', 'true']:
        return None
    return None

def sanitize_list(lst):
    sanitized = []
    for item in lst:
        if 'S' in item:
            value = sanitize_string(item['S'])
            if value:
                sanitized.append(value)
        elif 'N' in item:
            value = sanitize_number(item['N'])
            if value is not None:
                sanitized.append(value)
        elif 'BOOL' in item:
            value = sanitize_boolean(item['BOOL'])
            if value is not None:
                sanitized.append(value)
        elif 'NULL' in item:
            value = sanitize_null(item['NULL'])
            if value is not None:
                sanitized.append(value)
    return sanitized

def transform_input(input_data):
    output = []

    map_1 = input_data.get('map_1', {}).get('M', {})
    if map_1:
        transformed_map = {}
        
        list_1 = map_1.get('list_1', {}).get('L')
        if list_1 is not None:
            sanitized_list = []
            for item in list_1:
                if 'N' in item:
                    number = item['N'].strip().lstrip('0')
                    if number and number.replace('.', '').isdigit():
                        sanitized_list.append(float(number))
                elif 'BOOL' in item:
                    bool_value = item['BOOL'].strip().lower()
                    if bool_value in ['1', 't', 'true']:
                        sanitized_list.append(True)
                    elif bool_value in ['0', 'f', 'false']:
                        sanitized_list.append(False)
                elif 'NULL' in item:
                    null_value = item['NULL'].strip().lower()
                    if null_value in ['1', 't', 'true']:
                        sanitized_list.append(None)
            
            transformed_map['list_1'] = sanitized_list if sanitized_list else None
        
        null_1 = map_1.get('null_1', {}).get('NULL ')
        if null_1 is not None:
            null_value = null_1.strip().lower()
            if null_value in ['1', 't', 'true']:
                transformed_map['null_1'] = None
        
        if transformed_map:
            output.append({'map_1': transformed_map})

    number_1 = input_data.get('number_1', {}).get('N')
    if number_1 is not None:
        number = number_1.strip().lstrip('0')
        if number and number.replace('.', '').isdigit():
            output.append({'number_1': float(number)})

    string_1 = input_data.get('string_1', {}).get('S')
    if string_1 is not None:
        output.append({'string_1': string_1.strip()})

    string_2 = input_data.get('string_2', {}).get('S')
    if string_2 is not None:
        try:
            dt = datetime.datetime.strptime(string_2, '%Y-%m-%dT%H:%M:%SZ')
            unix_timestamp = int(dt.timestamp())
            output.append({'string_2': unix_timestamp})
        except ValueError:
            pass

    return output

# Parse input JSON
input_data = json.loads(input_json2)

# Transform input
output = transform_input(input_data)

# Convert list of dictionaries to a single dictionary
output_dict = {}
for item in output:
    output_dict.update(item)

# Print output JSON
output_json = json.dumps([output_dict], indent=2)
print(output_json)

