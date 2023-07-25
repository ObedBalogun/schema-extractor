import json


class SchemaExtractor:
    """
    This class provides methods to extract schemas from json files
    and copy them into new schema files
    """

    def __init__(self):
        self.first_file = "./data/data_1.json"
        self.second_file = "./data/data_2.json"

    def extract_schema_from_files(self):
        """
        Extract schemas from JSON files and generate new schema files.
        :return:
        """
        for file_name, json_file in self.__dict__.items():
            overall_schema = {}
            with open(json_file) as data_file:
                string_file = json.load(data_file)
                try:
                    schema_objects = string_file['message']
                    for key, value in schema_objects.items():
                        current_schema = {}
                        if type(value) in [str, int, bool, list]:
                            current_schema.update(self.determine_data_type(value, key))
                        else:
                            for obj_key, obj in schema_objects[key].items():
                                current_schema.update({obj_key: self.determine_data_type(obj, obj_key)})
                        overall_schema[key] = current_schema
                except KeyError as e:
                    return e
            self.write_to_file(overall_schema, file_name)
        return "Schemas extracted and new schema files generated."

    def write_to_file(self, schema, input_file):
        """
        :param schema:
        :param input_file:
        :return: Status Message
        """
        if input_file.__contains__("first"):
            with open("./schema/schema_1.json", "w") as f:
                json.dump(schema, f, indent=4)
        else:
            with open("./schema/schema_2.json", "w") as f:
                json.dump(schema, f, indent=4)
        return "Files have been generated"

    def determine_data_type(self, obj, tag=None):
        """

        :param: data object type
        :param:data tag (Optional)
        :return: dictionary representing object properties
        """
        if isinstance(obj, str):
            return {
                "type": "STRING",
                "tag": tag or "",
                "description": "",
                "required": False
            }
        elif isinstance(obj, int):
            return {
                "type": "INTEGER",
                "tag": tag or "",
                "description": "",
                "required": False
            }
        elif isinstance(obj, dict):
            properties = {}
            for item_key, item_value in obj.items():
                properties[item_key] = self.determine_data_type(item_value, item_key)
            return properties
        elif isinstance(obj, bool):
            return {
                "type": "BOOLEAN",
                "tag": tag or "",
                "description": "",
                "required": False
            }
        else:
            if not obj:
                obj_type = "ARRAY"
            else:
                obj_type = "ENUM ARRAY" if isinstance(obj[0], str) else "ARRAY"
            return {
                "type": obj_type,
                "tag": tag or "",
                "description": "",
                "required": False
            }
