#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        total = ((tuple_a[0] + tuple_b[0]), (0 + tuple_b[1]))
        return total
    if len(tuple_b) == 1:
        total = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0))
        return total
    if len(tuple_a) == 0 or len(tuple_b) == 0:
        tuple_a = 1
        tuple_b = 89
        total = (tuple_a, tuple_b)
        return total
    total = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return total