#!/usr/bin/python3
"""
module with class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

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
