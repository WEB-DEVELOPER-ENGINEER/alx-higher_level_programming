#!/usr/bin/python3
"""Student to JSON with filter
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
            retrieves a dictionary representation of a Student instance
        '''
        if attrs:
            if not all(isinstance(attr, str) for attr in attrs):
                return self.__dict__
            else:
                odict = self.__dict__
                redict = {}
                for key in self.__dict__:
                    if type(odict[key]) in [list, dict, str, int, bool]:
                        if key in attrs:
                            redict[key] = odict[key]
                return redict
        else:
            return self.__dict__
