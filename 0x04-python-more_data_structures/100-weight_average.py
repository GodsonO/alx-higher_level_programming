#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list and len(my_list):
        _number = 0
        denominator = 0
        for tup in my_list:
            _number += (tup[0] * tup[1])
            denominator += tup[1]
        return (_number / denominator)
    return 0
