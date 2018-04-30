#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    i = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end="")
            total = total + 1
            i = i + 1
        except TypeError:
            i = i + 1
        except ValueError:
            i = i + 1
    print()
    return total
