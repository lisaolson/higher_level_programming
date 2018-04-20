#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    a = list(a_dictionary.keys())[0]
    for y in a_dictionary:
        if y > a:
            a = y
    return a
