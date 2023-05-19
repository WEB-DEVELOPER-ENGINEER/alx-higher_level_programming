#!/usr/bin/python3
"""Tuples addition"""


def add_tuple(tuple_a=(), tuple_b=()):
    '''
        a function that adds 2 tuples
    '''
    listt = []
    i = 0
    if (len(tuple_a) < 2):
        lendif = 2 - len(tuple_a)
        tuple_a = list(tuple_a)
        tuple_a.extend([0] * lendif)
    if (len(tuple_b) < 2):
        lendif = 2 - len(tuple_b)
        tuple_b = list(tuple_b)
        tuple_b.extend([0] * lendif)
    for elm1, elm2 in zip(tuple_a, tuple_b):
        i += 1
        j = (elm1 + elm2)
        listt.append(j)
        if (i == 2):
            break
    return tuple(listt)
