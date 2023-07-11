#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""
import sys

file_size = 0
stat_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
num = 0
try:
    for line in sys.stdin:
        token = line.split()
        if len(token) >= 2:
            a = num
            if token[-2] in stat_tally:
                stat_tally[token[-2]] += 1
                num += 1
            try:
                file_size += int(token[-1])
                if a == num:
                    num += 1
            except FileNotFoundError:
                if a == num:
                    continue
        if num % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(stat_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(stat_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(stat_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
