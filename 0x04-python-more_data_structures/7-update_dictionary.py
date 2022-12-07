#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        up_dic = {key:value}
        a_dictionary.update(up_dic)
    else:
        a_dictionary[key] = value
    return a_dictionary
