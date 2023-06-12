#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lengthA = len(tuple_a)
    lengthB = len(tuple_b)
# check for tuple_a
    if lengthA < 1:
        tuple_a = (0, 0)
    elif lengthA < 2:
        tuple_a = (tuple_a[0], 0)

# check for tuple_b
    if lengthB < 1:
        tuple_b = (0, 0)
    elif lengthB < 2:
        tuple_b = (tuple_b[0], 0)

    res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return res
