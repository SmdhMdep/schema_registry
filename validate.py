import json
from jsonschema import validate, ValidationError


def validate_json(data_file, schema_file):
    try:
        with open(data_file, 'r') as data:
            json_data = json.load(data)
        with open(schema_file, 'r') as schema:
            json_schema =json.load(schema)
        validate(instance =json_data, schema = json_schema)
    except ValidationError as e:
        print(f"Validation failed: {e}")

data_file = 'data.json'
schema_file = 'schema.json'
validate_json(data_file, schema_file)
