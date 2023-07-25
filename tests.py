import unittest
import json
from schema_extractor import SchemaExtractor

class TestSchemaExtractor(unittest.TestCase):

    def setUp(self):
        self.schema_extractor = SchemaExtractor()

    def test_extract_schema_from_files(self):
        # Run the extract_schema_from_files method
        message = self.schema_extractor.extract_schema_from_files()

        # Check if the method returns the correct message
        self.assertEqual(message, "Schemas extracted and new schema files generated.")

        with open("./schema/schema_1.json", "r") as f:
            schema_content = json.load(f)
            self.assertGreater(len(schema_content), 0, "schema_1.json is empty.")

    def test_determine_data_type(self):
        # Test with different data types
        str_properties = self.schema_extractor.determine_data_type("Data2bots")
        self.assertEqual(str_properties, {
            "type": "STRING",
            "tag": "",
            "description": "",
            "required": False
        })

        int_properties = self.schema_extractor.determine_data_type(2)
        self.assertEqual(int_properties, {
            "type": "INTEGER",
            "tag": "",
            "description": "",
            "required": False
        })

        bool_properties = self.schema_extractor.determine_data_type(True)
        self.assertEqual(bool_properties, {
            "type": "BOOLEAN",
            "tag": "",
            "description": "",
            "required": False
        })

        enum_properties = self.schema_extractor.determine_data_type({"key_one": "value_one", "key_two": "value_two"})
        self.assertEqual(enum_properties, {
            "key_one": {
                "type": "STRING",
                "tag": "key_one",
                "description": "",
                "required": False
            },
            "key_two": {
                "type": "STRING",
                "tag": "key_two",
                "description": "",
                "required": False
            }
        })

        array_properties = self.schema_extractor.determine_data_type(["item1", "item2"])
        self.assertEqual(array_properties, {
            "type": "ENUM ARRAY",
            "tag": "",
            "description": "",
            "required": False
        })

if __name__ == '__main__':
    unittest.main()
