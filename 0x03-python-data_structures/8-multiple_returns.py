#!/usr/bin/python3
"""tuples"""


def multiple_returns(sentence):
    '''
        a func that returns a tuple with the len of a str and its first char
    '''
    if not sentence:
        sentence = None
        tup = (0, sentence)
    else:
        tup = (len(sentence), sentence[0])
    return tup
