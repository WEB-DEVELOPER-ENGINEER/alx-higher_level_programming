#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Max integer - Unittest
    """
    def test_no_args(self):
        '''
            Test for when there are no arguments
        '''
        self.assertEqual(max_integer(), None)

    def test_none(self):
        '''
            Test for when passing None
        '''
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string(self):
        '''
            Test for when a string is passed with ints
        '''
        with self.assertRaises(TypeError):
            max_integer([1, "hi"])

    def test_float(self):
        '''
            Test for when passing floats
        '''
        self.assertEqual(max_integer([1, 2.5]), 2.5)

    def test_output(self):
        '''
            Testing arguments
        '''
        self.assertEqual(max_integer([1, 2]), 2)

    def test_empty_list(self):
        '''
            Test for when passing empty list
        '''
        self.assertIsNone(max_integer([]))

    def test_negative(self):
        '''
            Test negative numbers
        '''
        self.assertEqual(max_integer([-3, -2]), -2)

    def test_single_arg(self):
        '''
            Test for when a list contains one item
        '''
        self.assertEqual(max_integer([59]), 59)

    def test_same_items(self):
        '''
            Test for when passing a list containing the same items
        '''
        self.assertEqual(max_integer([2, 2]), 2)

    def test_integer(self):
        '''
            Test for when passing an integer
        '''
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_beginning(self):
        '''
            Test for when the max  is at the beginning
        '''
        self.assertEqual(max_integer([100, 50, 20, 2]), 100)


if __name__ == "__main__":
    unittest.main()
