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

    @staticmethod
    def from_json_string(json_string):
        '''
             returns the list of the JSON string representation json_string
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            returns an instance with all attributes already set
        '''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            dummy = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            dummy = Square(5)
        dummy.update(**dictionary)
        return (dummy)
