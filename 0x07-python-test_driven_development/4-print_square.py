#!/usr/bin/python3
'''
Print square
'''


def print_square(size):
    """
    a function that prints a square with the character #
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
