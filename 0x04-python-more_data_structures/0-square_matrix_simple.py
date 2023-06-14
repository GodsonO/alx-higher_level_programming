#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x * x, _row)) for _row in matrix])
