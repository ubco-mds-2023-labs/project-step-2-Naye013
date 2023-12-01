import os
import json
import xml.etree.ElementTree as ET
import csv

class Config:
    def __init__(self, path_file, data_type, entity_collection, base_fields, computable_fields):
        self.path_file = path_file
        self.data_type = data_type
        self.entity_collection = entity_collection
        self.base_fields = base_fields
        self.computable_fields = computable_fields

    def is_valid_config(self):
        # Check if the file path exists
        if not os.path.exists(self.path_file):
            print(f"Error: File '{self.path_file}' does not exist.")
            return False

        # Extract the file extension
        _, file_extension = os.path.splitext(self.path_file)

        # Check if the file extension corresponds to a valid data type
        valid_extensions = {'.json': 'JSON', '.xml': 'XML', '.csv': 'CSV'}
        if file_extension.lower() not in valid_extensions:
            print(f"Error: Invalid file type for '{self.path_file}'. Supported types are JSON, XML, and CSV.")
            return False

        # Check if the specified data type matches the detected file extension
        if self.data_type != valid_extensions[file_extension.lower()]:
            print(f"Error: Data type '{self.data_type}' does not match the file extension for '{self.path_file}'.")
            return False

        return True

    def read_config(self):
        if not self.is_valid_config():
            return "Configuration not valid"  # If configuration is not valid return a message

        config_data = {}

        if self.data_type == 'JSON':
            with open(self.path_file, 'r') as json_file:
                config_data = json.load(json_file)

        elif self.data_type == 'XML':
            tree = ET.parse(self.path_file)
            root = tree.getroot()
            config_data['entity_collection'] = self.entity_collection
            config_data['base_fields'] = [field.text for field in root.findall('.//base_fields/field')]
            config_data['computable_fields'] = [field.text for field in root.findall('.//computable_fields/field')]

        elif self.data_type == 'CSV':
            with open(self.path_file, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                config_data['entity_collection'] = self.entity_collection
                config_data['base_fields'] = csv_reader.fieldnames
                config_data['computable_fields'] = [field for field in config_data['base_fields'] if field not in self.base_fields]

        return config_data
