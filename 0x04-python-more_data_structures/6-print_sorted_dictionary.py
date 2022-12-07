#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for keys in sorted(list(my_dict)):
        print('{}: {}'.format(keys, my_dict[keys]))
