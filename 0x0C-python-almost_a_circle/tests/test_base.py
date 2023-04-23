#!/usr/bin/python3
import sys
import unittest
sys.path.append('../models')
from base import Base
"""unittest for Base class
"""


class TestBase(unittest.TestCase):
    '''
        Testing the class Base
    '''
    def test_id(self):
        '''
            Testing the public instance attribute id
        '''
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
