#!/usr/bin/python3
"""
This function prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for y in text:
        if flag == 0:
            if y == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if y == '?' or y == '.' or y == ':':
                print(y)
                print()
                flag = 0
            else:
                print(y, end="")
