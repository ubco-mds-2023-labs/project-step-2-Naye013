import os
import json
import csv
import xml.etree.ElementTree as ET

class Config:
    """
    Config class for handling configuration read and write operations.

    Attributes:
    - file_path (str): The path to the configuration file.
    - config (dict): The configuration data.

    Methods:
    - is_valid_config(): Check if a valid configuration is present.
    - is_valid_path(): Check if the file path has a valid format.
    - read_config(): Read configuration from the file.
    - write_config(file_path=None): Write configuration to the file.
    """

    SUPPORTED_FORMATS = ['.json', '.csv', '.xml']

    def __init__(self, file_path='config.json'):
        """
        Initialize the Config object.

        Parameters:
        - file_path (str): The path to the configuration file.
        """
        # Check if the provided file path has a valid format
        if not self.is_valid_path(file_path):
            raise ValueError(f"Invalid file path: {file_path}. Please provide an absolute or relative file path with a valid format.")
        
        self.file_path = file_path
        self.config = None
        self.supported_formats = self.SUPPORTED_FORMATS

    def is_valid_path(self, path):
        """
        Check if the provided file path has a valid format.

        Parameters:
        - path (str): The file path to be validated.

        Returns:
        - bool: True if the path has a valid format, False otherwise.
        """
        # Check if the path is an absolute or relative file path
        if not os.path.isabs(path) and not os.path.relpath(path):
            print(f"Invalid file path: {path}. Please provide an absolute or relative file path.")
            return False

        if not any(path.endswith(fmt) for fmt in self.SUPPORTED_FORMATS):
            print(f"Unsupported file format: {path}")
            return False

        return True

    def read_config(self):
        """
        Read configuration from the file.

        Returns:
        - dict or None: The configuration data if read successfully, None otherwise.
        """
        try:
            # Check if the file format is supported
            if not self.is_valid_path(self.file_path):
                print(f"Unsupported file format: {self.file_path}")
                return None

            # Check if the file exists
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"Config file not found at {self.file_path}. Please, use write_config to create a new one.")

            # Read configuration based on the file format
            if self.file_path.endswith('.json'):
                with open(self.file_path, 'r') as file:
                    self.config = json.load(file)
            elif self.file_path.endswith('.csv'):
                with open(self.file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    self.config = dict(reader)
            elif self.file_path.endswith('.xml'):
                tree = ET.parse(self.file_path)
                root = tree.getroot()
                self.config = {}
                for elem in root:
                    self.config[elem.tag] = elem.text

            return self.config
        except Exception as e:
            print(f"Error reading config file at {self.file_path}: {e}")
            return None

    def write_config(self, file_path=None):
        """
        Write configuration to the file.

        Parameters:
        - file_path (str): The path to the configuration file.
        """
        if file_path:
            # Check if the provided file path has a valid extension
            if not self.is_valid_path(file_path):
                print(f"Unsupported file format: {file_path}")
                return
            self.file_path = file_path

        config_data = {}

        # User input to set configuration
        config_data['data_source'] = self.get_valid_input("Enter data source: ", is_file_path=True)
        config_data['data_destination'] = self.get_valid_input("Enter data destination: ", is_file_path=True)

        try:
            # Write configuration based on the file format
            if self.file_path.endswith('.json'):
                with open(self.file_path, 'w') as file:
                    json.dump(config_data, file, indent=2)
            elif self.file_path.endswith('.csv'):
                with open(self.file_path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=config_data.keys())
                    writer.writeheader()
                    writer.writerow(config_data)
            elif self.file_path.endswith('.xml'):
                root = ET.Element("config")
                for key, value in config_data.items():
                    elem = ET.SubElement(root, key)
                    elem.text = str(value)
                tree = ET.ElementTree(root)
                tree.write(self.file_path)
            else:
                print(f"Unsupported file format: {self.file_path}")
                return

            self.config = config_data
            print(f"Configuration written to {self.file_path}")
        except Exception as e:
            print(f"Error writing config file at {self.file_path}: {e}")

    def get_valid_input(self, prompt, is_file_path=False):
        """
        Get valid user input.

        Parameters:
        - prompt (str): The prompt to display.
        - is_file_path (bool): Whether the input should be validated as a file path.

        Returns:
        - str: Valid user input.
        """
        while True:
            user_input = input(prompt)
            if not user_input.strip():
                print("Input cannot be empty. Please try again.")
            elif is_file_path and not self.is_valid_path(user_input):
                print(f"Invalid file path: {user_input}. Please provide a valid file path.")
            else:
                return user_input
