#!/usr/bin/python3
"""Module to define check for same class
"""


def is_same_class(obj, a_class):
    """Checks if obj is an exact instance of class

    Returns:
        True if match, False if not
    """
    if type(obj) == a_class:
        return True
    return False
