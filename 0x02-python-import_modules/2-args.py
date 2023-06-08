#!/usr/bin/python3
import sys


def main():
    num_arg = len(sys.argv) - 1
    if num_arg == 0:
        print("0 arguments.")
    elif num_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arg))
    for i in range(num_arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))


if __name__ == "__main__":
    main()
