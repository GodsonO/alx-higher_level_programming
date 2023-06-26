#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    nex_t = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            nex_t += 1
        except IndexError:
            break
    print()
    return nex_t
