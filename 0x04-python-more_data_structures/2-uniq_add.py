#!/usr/bin/python3


def uniq_add(my_list=[]):
    add_num = 0
    for i in set(my_list):
        add_num = add_num + i
    return add_num
