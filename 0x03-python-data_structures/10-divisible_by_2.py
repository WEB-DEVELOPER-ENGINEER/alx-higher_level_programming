#!/usr/bin/python3
"""multiples of 2"""


def divisible_by_2(my_list=[]):
    '''
        a function that finds all multiples of 2 in a list
    '''
    boolist = my_list[:]
    for j, i in enumerate(my_list):
        if i % 2 == 0:
            boolist[j] = True
        else:
            boolist[j] = False
    return(boolist)
