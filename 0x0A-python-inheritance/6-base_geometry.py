#!/usr/bin/python3
'''
based on 5-base_geometry.py
'''


Base = __import__('5-base_geometry').BaseGeometry
class BaseGeometry(Base):
    def area(self):
        raise Exception("area() is not implemented")
