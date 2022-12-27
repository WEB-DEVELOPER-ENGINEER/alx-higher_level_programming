#!/usr/bin/python3
'''
A class Square that defines a square
'''


class Square:
    '''A class that defines a square
    '''
    def __init__(self, size=0, position=(0, 0)):
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
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        slef.__position = value