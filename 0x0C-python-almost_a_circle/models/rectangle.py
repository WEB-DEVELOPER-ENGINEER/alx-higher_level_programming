#!/usr/bin/python3
"""First Rectangle
"""


from models.base import Base


class Rectangle(Base):
    '''
        class Rectangle that inherits from Base
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            Class constructor
        '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.setter_checker("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.setter_checker("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.setter_checker("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.setter_checker("y", value)
        self.__y = value

    @staticmethod
    def setter_checker(attr, val):
        if type(val) != int:
            raise TypeError("{} must be an integer".format(attr))
        if attr == "x" or attr == "y":
            if val < 0:
                raise ValueError("{} must be >= 0".format(attr))
        elif val <= 0:
            raise ValueError("{} must be > 0".format(attr))
