#!/usr/bin/python3
"""Student to disk and reload
"""


class Student:
    '''
        a class Student that defines a student
    '''
    def __init__(self, first_name, last_name, age):
        '''
            Instantiation with first_name, last_name and age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
            retrieves a dict representation of a Student instance
        '''
        odict = {}
        if type(attrs) == list and all(isinstance(j, str) for j in attrs):
            for i in attrs:
                try:
                    odict[i] = getattr(self, i)
                except Exception:
                    pass
        else:
            odict = self.__dict__
        return odict

    def reload_from_json(self, json):
        '''
            Public method to replace all attributes of the Student instance
        '''
        for key, value in json.items():
            self.__setattr__(key, value)
