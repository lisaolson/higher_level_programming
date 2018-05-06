#!/usr/bin/python3
"""Module to print a square of given size
"""
def print_square(size):
    """Prints a square of given size

    Args:
        size (int): size of square to print

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is a negative number

    Returns:
        None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(0, size):
        for y in range(0, size):
            print('#', end="")
        print()
