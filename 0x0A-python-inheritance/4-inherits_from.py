#!/usr/bin/python3
"""Module to check if obj is a sub class
"""


def inherits_from(obj, a_class):
    """Checks if object is a sub class

    Returns:
        True if it is, false if not
    """
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    return False
