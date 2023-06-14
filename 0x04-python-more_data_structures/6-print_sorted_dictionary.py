#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    dictionary = sorted(a_dictionary.keys())
    for key in dictionary:
        print("{:s}: {}".format(key, a_dictionary[key]))
