#!/usr/bin/python3
"""Delete at"""


def delete_at(my_list=[], idx=0):
    '''
        a function that deletes an item at a specific position in a list
    '''
    if 0 <= idx < len(my_list):
        del(my_list[idx])
    return(my_list)
