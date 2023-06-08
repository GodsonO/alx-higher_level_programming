#!/usr/bin/python3
import sys


def main():
    num_arg = len(sys.argv)
    if num_arg == 1:
        print('0')
    else:
        sum = 0
        for i in range(1, num_arg):
            sum += int(sys.argv[i])
        print("{:d}".format(sum))


if __name__ == "__main__":
    main()
