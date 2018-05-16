#!/usr/bin/python3
"""Module to check if obj is instance of class
"""


def is_kind_of_class(obj, a_class):
    """Checks if object is instance of class

    Returns:
        True if match, false if not
    """

    if isinstance(obj, a_class):
        return True
    return False
