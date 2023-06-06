#!/usr/bin/python3
for digit_1 in range(0, 8):
    for digit_2 in range(digit_1 + 1, 10):
        print("{:d}{:d}".format(digit_1, digit_2), end=', ')
print("{:d}{:d}".format(digit_1 + 1, digit_2))
