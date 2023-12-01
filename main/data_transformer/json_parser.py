import os
import json
from data_transformer.abstract_parser import Parser
from data_processor.entity import EntityCollection as EC

class JsonParser(Parser):
    type = "JSON"
    def __init__(self, config):
        super().__init__(self)
        self.config = config
        self.entityCollection = EC()

    def parse(self):
        data = self.__validate__()
        if self.config.entity_collection in data:
            entities = data[self.config.entity_collection]
            parsed_expressions = self.get_parsed_expression()
            fields = self.get_computable_fields()
            for entity in entities:
                entity_object = self.entityCollection.add_entity(value=entity.get(self.config.base_field))
                self.__handle_normal_fields__(entity, fields, entity_object)
                self.__handle_expression_fields__(entity, parsed_expressions, entity_object)
        return self.entityCollection

    def __handle_normal_fields__(self, entity, fields, entity_object):
        '''Prinitng for testing purposes'''
        # print(entity.get(self.config.base_field))
        for field in fields:
            entity_object.add(field, entity.get(field))

    def __handle_expression_fields__(self, entity, parsed_expressions, entity_object):
        for expression in parsed_expressions:
            self.evaluate_expression(entity.get(expression[0]), entity.get(expression[1]),
                                     expression[2], expression[3], entity_object)

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

