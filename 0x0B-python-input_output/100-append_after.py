#!/usr/bin/python3
"""Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    '''
        adds a text to a file after each line containing a specific string
    '''
    str_to_write = ""
    with open(filename, encoding="utf8") as f:
        for line in f:
            str_to_write += line
            if search_string in line:
                str_to_write += new_string 
    with open(filename, mode="w") as f:
        f.write(str_to_write)
