#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        x = 0
        s = ''
        for k, v in a_dictionary.items():
            if v > x:
                x = v
                s = k
        return s
    else:
        return None
