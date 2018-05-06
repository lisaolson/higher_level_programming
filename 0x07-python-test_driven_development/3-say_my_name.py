#!/usr/bin/python3
"""Module to print My name is followed by first and last name
"""
def say_my_name(first_name, last_name=""):
    """Prints 'My name is' followed by first and last name given
    Args:
        first_name (str): First name
        last_name (str): Last name

    Raises:
        TypeError: If first or last name is not a string

    Returns:
        None
    """

    if first_name is None:
        raise TypeError("first_name must be a string")
    if last_name is None:
        raise TypeError("last_name must be a string")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
