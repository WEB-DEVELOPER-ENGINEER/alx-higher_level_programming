#!/usr/bin/python3
'''
Text indentation
'''


def text_indentation(text):
    """
    prints a text with 2 new lines after these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for c in range(len(text)):
        if (text[c] == "." or text[c] == "?" or text[c] == ":"):
            print(text[c], end='\n\n')
        else:
            if (c + 1 < len(text) and text[c + 1] == " "):
                print(text[c].lstrip(), end=' ')
            else:
                print(text[c].lstrip(), end='')
