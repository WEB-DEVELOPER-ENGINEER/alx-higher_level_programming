#!/usr/bin/python3
"""Base class
"""
import json
import csv
import os


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

    @classmethod
    def load_from_file(cls):
        '''
            returns a list of instances
        '''
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, encoding="UTF8") as f:
                string = cls.from_json_string(f.read())
        except Exception:
            return []
        instances = []
        for instance in string:
            tmp = cls.create(**instance)
            instances.append(tmp)
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
            serializes in CSV
        '''
        file_name = cls.__name__ + ".csv"
        with open(file_name, mode="w", newline='', encoding="UTF8") as f:
            write_this = csv.writer(f, delimiter=" ")
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(obj["id"]) + "," + str(obj["width"]) + "," +
                               str(obj["height"]) + "," +
                               str(obj["x"]) + "," + str(obj["y"]))
                    write_this.writerow(string)
            if cls.__name__ == "Square":
                for obj in list_objs:
                    string = ""
                    obj = obj.to_dictionary()
                    string += (str(obj["id"]) + "," + str(obj["size"]) + "," +
                               str(obj["x"]) + "," + str(obj["y"]))
                    write_this.writerow(string)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        new_list = []
        file_name = cls.__name__ + '.csv'
        if os.path.exists(file_name) is True:
            with open(file_name, "r") as csvfile:
                dictreader = csv.DictReader(csvfile)
                new_list = [dict([key, int(value)] for key, value
                                in dictionary.items()) for dictionary
                           in dictreader]
            for i in range(len(new_list)):
                new_list[i] = cls.create(**new_list[i])
        return new_list
