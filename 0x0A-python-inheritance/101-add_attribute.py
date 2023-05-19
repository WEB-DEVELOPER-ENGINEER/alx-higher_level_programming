#!/usr/bin/python3
"""Add attr to an obj"""

def add_attribute(obj, name, value):
    '''
        a function that adds a new attribute to an object if it’s possible
    '''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
