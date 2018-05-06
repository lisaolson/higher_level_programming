#!/usr/bin/python3
"""Module to find result of adding two integers
"""

def add_integer(a, b=98):
    """Adds integer a and integer b and returns result

    Args:
        a (int): integer a to add
        b (int): integer b with optional value 98

    Raises:
        TypeError: If a or b is not an integer or float

    Returns:
        Total of integer a and integer b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
