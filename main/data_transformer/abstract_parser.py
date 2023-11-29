import re

class Parser():
    def __init__(self,config):
        self.config = config
        self.__parsed_expression_collection__ =[]
    
    def Parse(self):
        pass
    
    def get_computable_fields(self):
        fields = set()
        for field in self.config.Computable_Fields:
            if "+" in field:
                self.__parse_expression__("+", field)
            elif "-" in field:
                self.__parse_expression__("-", field)
            elif "*" in field:
                self.__parse_expression__("*", field)
            elif "/" in field:
                self.__parse_expression__("/", field)
            else:
                fields.add(field)
        return fields
      
    def get_parsed_expression(self):
        return self.__parsed_expression_collection__
    
    def evaluate_expression(self,first_term, second_term, alias, operator):
        '''NOTE: Printing as of now.As Entity.py is not ready'''
        if "+" == operator:
            print(alias, " : ", first_term+second_term)
        if "-" == operator:
            print(alias, " : ", first_term-second_term)
        if "*" == operator:
            print(alias, " : ", first_term*second_term)
        if "/" == operator:
            print(alias, " : ", first_term/second_term)
                
    def __parse_expression__(self,dynamic_splitter, field):
        pattern = r'\s*(?:[{}\s]|as)\s*'.format(dynamic_splitter)
        matches = re.split(pattern, field)
        self.__store_parsed_expression__(matches,dynamic_splitter)
        
    def __store_parsed_expression__(self,expression_collection,function):
        expression_collection.append(function)
        self.__parsed_expression_collection__.append(expression_collection)  
        
    