#!/usr/bin/python3
'''
A class Square that defines a square.
This module provides a simple Square class with initialize size.
Attribute position which takes a default (0, 0) tuple.
'''


class Square:
    '''A class that defines a square
    Also defines position using a tuple, which defaults (0, 0).
    '''
    def __init__(self, size=0, position=(0, 0)):
        if type(position) != tuple or len(position) != 2 or position[0] != int \
                or position[1] != int or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(0, self.__size):
                x = 0
                for i in range(0, self.__size):
                    if x == 0:
                        for i in range(0, self.__position[0]):
                            print(" ", end="")
                            x += 1
                    print("#", end="")
                print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or value[0] != int \
                or value[1] != int or value[0] <= 0 or value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
