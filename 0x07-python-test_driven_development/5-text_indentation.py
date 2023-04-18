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
    line = ""
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            lines.append(line.strip() + text[i])
            line = ""
            special_char = True
        else:
            line += text[i]
            special_char = False
    if line:
        lines.append(line.strip())
    for i, line in enumerate(lines):
        if line:
            print(line, end="")
            if i < len(lines) - 1 or special_char:
                print("\n")
