#!/usr/bin/python3
"""Base class
"""
import json


class Base:
    '''
        the first class Base
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
            class constructor
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
            returns the JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            writes the JSON string representation of list_objs to a file
        '''
        file_name = cls.__name__ + ".json"

        string = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                string.append(json_dict)

        with open(file_name, mode="w") as f:
            json.dump(string, f)
