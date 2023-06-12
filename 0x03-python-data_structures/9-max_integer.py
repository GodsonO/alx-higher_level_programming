#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    big_integer = my_list[0]
    for i in my_list:
        if i > big_integer:
            big_integer = i
    return (big_integer)
