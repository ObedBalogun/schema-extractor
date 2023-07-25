from schema_extractor import SchemaExtractor

def extract_schema():
    schema_extractor = SchemaExtractor()
    program_status = schema_extractor.extract_schema_from_files()
    print(program_status)


if __name__ == "__main__":
    extract_schema()