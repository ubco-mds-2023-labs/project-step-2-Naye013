import os
import json
import difflib

class Config:
    def __init__(self):
        """
        Initializes a Config instance.

        Attributes:
            path (str): Absolute or relative path from the file in the configuration file.
            data_type (str): The type of data in the configuration file (e.g., 'JSON', 'XML', 'CSV').
            entity_collection (str): The collection of entities in the data.
            base_field (str): The base field used in the configuration.
            computable_fields (list): A list of computable fields in the configuration.
            config_data (dict): The configuration data read from the file.
        """
        self.data_type = ''
        self.entity_collection = ''
        self.base_field = ''
        self.computable_fields = []
        self.path = os.path.join(os.getcwd(), 'config.json')
        self.config_data = self.read_config()

    def is_valid_config(self):
        """
        Checks if the configuration is valid.

        Returns:
            bool: True if the configuration is valid, False otherwise.
        """
        # Check if the file path exists
        if not os.path.exists(self.path):
            print(f"Error: File '{self.path}' does not exist.")
            return False

        # Extract the file extension
        _, file_extension = os.path.splitext(self.path)

        # Check if the file extension corresponds to a valid data type or a close match
        valid_extensions = ['.json', '.xml', '.csv']
        if file_extension.lower() not in valid_extensions:
            # Find close matches using difflib
            close_matches = difflib.get_close_matches(file_extension.lower(), valid_extensions)
            
            # Display an error message with close matches
            print(f"Error: Invalid file type for '{self.path}'. "
                  f"Supported types are JSON, XML, and CSV. Close matches: {', '.join(close_matches)}")
            
            return False

        return True

    def read_config(self):
        """
        Reads the configuration data from the file and initializes attributes.

        Returns:
            dict: The configuration data.
        """
        if not self.is_valid_config():
            return "Configuration not valid"  # If configuration is not valid return a message

        # Read the configuration from the existing file
        try:
            with open(self.path, 'r') as json_file:
                config_data = json.load(json_file)

            # Initialize attributes based on the configuration data
            self.path = config_data.get('path', '')
            self.data_type = config_data.get('data_type', '')
            self.entity_collection = config_data.get('entity_collection', '')
            self.base_field = config_data.get('base_field', '')
            self.computable_fields = config_data.get('computable_fields', [])

            return config_data
        
        # Prints an error message indicating a failure to read the configuration from the specified file,
        # including the specific exception details, and returns None to signal an unsuccessful read operation
        except Exception as e:
            print(f"Error reading configuration from '{self.path}': {e}")
            return None

    def get(self, property_name):
        """
        Retrieves the value of a property.

        Parameters:
            property_name (str): The name of the property to retrieve.

        Returns:
            Any: The value of the specified property.
        """
        return getattr(self, property_name, None)
