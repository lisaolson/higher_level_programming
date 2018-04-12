#!/usr/bin/python3
for i in range(90):
    if i == 89:
        print("{:d}".format(i))
    elif (i % 10 > i / 10):
        print("{:02}".format(i), end=", ")
