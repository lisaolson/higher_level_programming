#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    a = 0
    for x in my_list:
        if x > a:
            a = x
    return a
