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

    def __init__(self, file_path):
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
    

    def write_config(self, file_path=None):
        """
        Write configuration to the file.

        Parameters:
        - file_path
        """
