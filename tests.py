import unittest
import pathlib
import json
import string
import contextlib

from jsonschema import validators, SchemaError
from hypothesis import given
from hypothesis import strategies as st


def dict_without(value, key):
    """Return a new dict with key removed."""
    result = dict(value)
    result.pop(key)
    return result


def text_st(min_size=0, max_size=None):
    return st.text(alphabet=string.printable, min_size=min_size, max_size=max_size)


def schema(**kwargs):
    return st.builds(dict, **kwargs)


def root_schema(property_schema_st = st.just({})):
    return st.fixed_dictionaries({
        "title": text_st(min_size=5, max_size=60),
        "description": text_st(),
        "$schema": st.just("https://iot.smdh.uk/meta-schema#"),
        "type": st.just("object"),
        "properties": property_schema_st,
    })


VALID_TYPES = ("array", "boolean", "integer", "null", "number", "object", "string")
VALID_MVDTYPES = ("int", "long", "float", "double")


class MetaSchemaTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with open('meta-schema') as f:
            self.meta_schema = json.load(f)
        self.validator = validators.create(self.meta_schema)

    def test_meta_schema_is_valid(self):
        meta_schema_validator = validators.validator_for(self.meta_schema)
        meta_schema_validator.check_schema(self.meta_schema)

    BASE_SCHEMA = {
        "title": "Test Schema",
        "description": "test description",
        "$schema": "https://iot.smdh.uk/meta-schema#",
        "type": "object",
        "properties": {},
    }
    TEST_SCHEMAS = [
        [ "schema must not be empty", False, {} ],
        [ "a base schema with no properties is valid", True, BASE_SCHEMA ],
        [ "schema must have a 'title' field", False, dict_without(BASE_SCHEMA, "title") ],
        [ "schema must have a 'description' field", False, dict_without(BASE_SCHEMA, "description") ],
        [ "schema must have a '$schema' field", False, dict_without(BASE_SCHEMA, "$schema") ],
        [ "schema must have a 'type' field", False, dict_without(BASE_SCHEMA, "type") ],
        [ "schema must have a 'properties' field", False, dict_without(BASE_SCHEMA, "properties") ],
        [ "schema 'type' must be 'object'", False, dict_without(BASE_SCHEMA, "properties") ],
        [ "schema title must not exceed 60 characters limit", False, { **BASE_SCHEMA,
            "title": ''.join(string.ascii_letters[i % len(string.ascii_letters)] for i in range(62)),
        } ],
        [ "schema title cannot be empty", False, { **BASE_SCHEMA,
            "title": '',
        } ],
        [ "schema title must be of at least 5 characters", False, { **BASE_SCHEMA,
            "title": ''.join(letter for letter, _ in zip(string.ascii_letters, range(4))),
        } ],
        [ "a base schema with a simple property is valid", True, { **BASE_SCHEMA,
            "properties": {
                "value": { "type": "string" }
            }
        } ],
        [ "a base schema with multiple simple properties is valid", True, { **BASE_SCHEMA,
            "properties": {
                "value": { "type": "integer" },
                "name": { "type": "string" },
                "type": { "type": "string", "enum": ["typeA", "typeB"] }
            }
        } ],
        [ "properties sub-schemas must have a 'type' field", False, { **BASE_SCHEMA,
            "properties": {
                "type": { "enum": ["typeA", "typeB"] }
            }
        } ],
        [ "properties sub-schemas can have an mvDType", True, { **BASE_SCHEMA,
            "properties": {
                "value": {
                    "type": "string",
                    "mvDType": "int",
                }
            }
        } ],
        [ "properties sub-schemas can have an mvDType and must have a type", False, { **BASE_SCHEMA,
            "properties": {
                "value": { "mvDType": "int" }
            }
        } ],
        [ "'mvDType' field accepts int, long, double, and float", True, { **BASE_SCHEMA,
            "properties": {
                "value1": { "type": "string", "mvDType": "int" },
                "value1": { "type": "string", "mvDType": "long" },
                "value1": { "type": "string", "mvDType": "float" },
                "value1": { "type": "string", "mvDType": "double" },
            }
        } ],
    ]

    def test_meta_schema_expected_validation(self):
        stack = contextlib.ExitStack()
        for msg, valid, schema in self.TEST_SCHEMAS:
            with self.subTest(msg, valid=valid), stack:
                if not valid:
                    stack.enter_context(self.assertRaises(SchemaError))
                self.validator.check_schema(schema)

    @given(schema=root_schema())
    def test_validates_root_schema(self, schema):
        self.validator.check_schema(schema)

    @given(properties_schema=schema(
        value=schema(
            type=st.sampled_from(VALID_TYPES),
            mvDType=st.sampled_from(VALID_MVDTYPES),
    )))
    def test_validates_proper_types(self, properties_schema):
        schema = {**self.BASE_SCHEMA, "properties":properties_schema}
        self.validator.check_schema(schema)

    invalid_type_st = text_st().filter(lambda s: s not in VALID_TYPES)
    invalid_mvdtype_st = text_st().filter(lambda s: s not in VALID_MVDTYPES)

    @given(properties_schema=schema(
        id=st.one_of([
            schema(type=invalid_type_st),
            schema(type=st.just("string"), mvDType=invalid_mvdtype_st),
            schema(type=invalid_type_st, mvDType=invalid_mvdtype_st),
        ])
    ))
    def test_invalidates_improper_types(self, properties_schema):
        schema = {**self.BASE_SCHEMA, "properties":properties_schema}
        with self.assertRaises(SchemaError):
            self.validator.check_schema(schema)

    def test_devices_schemas_against_meta_schema(self):
        for schema_path in pathlib.Path().glob('[!.]*/**/*.json'):
            with self.subTest(path=str(schema_path)):
                with open(schema_path) as f:
                    schema = json.load(f)
                self.validator.check_schema(schema)


if __name__ == '__main__':
    unittest.main()
