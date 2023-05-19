#!/usr/bin/python3
'''
    My integer
'''


class MyInt(int):
    '''
        a class MyInt that inherits from int
    '''
    def __init__(self, number):
        '''
            Initialization
        '''
        self.number = number

    def __ne__(self, val):
        '''
            != operator inverted
        '''
        return (self.number == val)

    def __eq__(self, val):
        '''
            == operator inverted
        '''
        return (self.number != val)

    def __str__(self):
        '''
            returns a number
        '''
        return (str(self.number))
