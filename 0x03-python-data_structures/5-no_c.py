#!/usr/bin/python3
def no_c(my_string):
    strr = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            pass
        else:
            strr += i
    return strr
