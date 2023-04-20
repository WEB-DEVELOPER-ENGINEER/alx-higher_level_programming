#!/usr/bin/python3
"""Write to a file
"""


def write_file(filename="", text=""):
    '''
        writes a string to a text file (UTF8).
        returns the number of characters written
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
