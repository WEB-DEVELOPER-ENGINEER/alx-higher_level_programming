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
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line:
            lines.append(line)
    text = " ".join(lines)
    buff = ""
    for c in text:
        buff += c
        if c in [".", "?", ":"]:
            print(buff.strip())
            print()
            print()
            buff = ""
    if buff:
        print(buff.strip())
