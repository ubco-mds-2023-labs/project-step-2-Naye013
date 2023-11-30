import os
import xml.etree.ElementTree as ET
from data_transformer.abstract_parser import Parser

class XmlParser(Parser):
    type = "XML"

    def __init__(self, config):
        super().__init__(self)
        self.config = config

    def parse(self):
        root = self.__validate__()
        entities = root.findall(self.config.entity_collection)
        # print(entities)
        parsed_expressions = self.get_parsed_expression()
        fields = self.get_computable_fields()
        for entity in entities:
            self.__handle_normal_fields__(entity, fields)
            self.__handle_expression_fields__(entity, parsed_expressions)

    def __handle_normal_fields__(self, entity, fields):
        '''Prinitng as of now'''
        print(entity.get(self.config.base_field))
        for field in fields:
            print(entity.find(field).text)
            # print(entity.get(field))

    def __handle_expression_fields__(self, entity, parsed_expressions):
        for expression in parsed_expressions:
            self.evaluate_expression(entity.find(expression[0]).text, entity.find(expression[1]).text, expression[2], expression[3])

    def __validate__(self):
        file_Name = os.path.basename(self.config.path)
        if ".xml" not in file_Name:
            raise ValueError("XML PARSER: Incorrect Parser")
        try:
            data = self.__load_data__()
            if len(data.findall("student")) == 0:
                raise ValueError("XML PARSER: Configuration entity_Collection doesn't match")
            return data
        except:
            print("XML PARSER: Invalid Json")

    def __load_data__(self):
        tree = ET.parse(self.config.path)
        return tree.getroot()