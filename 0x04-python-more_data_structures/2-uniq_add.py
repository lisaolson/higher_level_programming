#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    my_list = list(uniq_set)
    total = 0
    for x in my_list:
        total += x
    return total
