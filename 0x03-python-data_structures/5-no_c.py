#!/usr/bin/python3
strr = ""
def no_c(my_string):
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            strr += i
    return strr
