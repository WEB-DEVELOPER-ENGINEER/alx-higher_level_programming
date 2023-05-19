#!/usr/bin/python3
"""
module with class Rectangle
"""


class BaseGeometry:
    '''
        BaseGeometry class
    '''
    def area(self):
        '''
            method for calculating area
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate if value is integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))


class Rectangle(BaseGeometry):
    '''
        Rectangle class
    '''
    def __init__(self, width, height):
        """Initialization"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
