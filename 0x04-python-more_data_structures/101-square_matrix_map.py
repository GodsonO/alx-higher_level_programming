#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda _row: list(map((lambda y: y * y), _row))), matrix))
