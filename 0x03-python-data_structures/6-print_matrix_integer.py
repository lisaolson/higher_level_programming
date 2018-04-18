#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for x in row:
            if x % 3 == 0:
                print("{:d}".format(x), end="\n")
            else:
                print("{:d}".format(x), end=" ")

