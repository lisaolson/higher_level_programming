#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for x in row:
                if x != row[-1]:
                    print("{:d}".format(x), end=" ")
                else:
                    print("{:d}".format(x), end="")
            print("")
