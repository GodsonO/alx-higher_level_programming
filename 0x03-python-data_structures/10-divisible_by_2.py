#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    newlist = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            newlist[i] = 1
        else:
            newlist[i] = 0
    return newlist
