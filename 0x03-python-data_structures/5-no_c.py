#!/usr/bin/python3
def no_c(my_string):
    new_str = []
    for x in my_string:
        if x != 'c' and x != 'C':
            new_str.append(x)
    new_str = "".join(new_str)
    return new_str
