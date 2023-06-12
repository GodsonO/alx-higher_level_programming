#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for in_list in matrix:
        print(" ".join("{:d}".format(j) for j in in_list))
