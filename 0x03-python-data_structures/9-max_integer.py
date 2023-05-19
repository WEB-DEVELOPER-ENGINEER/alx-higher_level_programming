#!/usr/bin/python3
"""Find the max"""


def max_integer(my_list=[]):
    '''
        a function that finds the biggest integer of a list
    '''
    if not my_list:
        return None
    ma_x = my_list[0]
    for i in my_list:
        if (ma_x < i):
            ma_x = i
    return ma_x
