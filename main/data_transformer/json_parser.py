import os
import json
from data_transformer.abstract_parser import Parser

class JsonParser(Parser):
    type = "JSON"
    def __init__(self, config):
        super().__init__(self)
        self.config = config

    def parse(self):
        data = self.__validate__()
        if self.config.entity_collection in data:
            entities = data[self.config.entity_collection]
            parsed_expressions = self.get_parsed_expression()
            fields = self.get_computable_fields()
            for entity in entities:
                self.__handle_normal_fields__(entity, fields)
                self.__handle_expression_fields__(entity, parsed_expressions)

    def __handle_normal_fields__(self, entity, fields):
        '''Prinitng as of now'''
        print(entity.get(self.config.base_field))
        for field in fields:
            print(entity.get(field))

    def __handle_expression_fields__(self, entity, parsed_expressions):
        for expression in parsed_expressions:
            self.evaluate_expression(entity.get(expression[0]), entity.get(expression[1]),
                                     expression[2], expression[3])

    def __validate__(self):
        file_Name = os.path.basename(self.config.path)
        if ".json" not in file_Name:
            raise ValueError("JSON PARSER: Incorrect Parser")
        try:
            data = self.__load_data__()
            if self.config.entity_collection not in data:
                raise ValueError("JSON PARSER: Configuration entity_Collection doesn't match")
            return data
        except:
            print("JSON PARSER: Invalid Json")

    def __load_data__(self):
        with open(self.config.path, 'r') as file:
            return json.load(file)

