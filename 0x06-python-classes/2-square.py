#!/usr/bin/python3
class Square:
    """
    Defines a square
    """
    def __init__(self, size=0):
        """
        Args:
            size (int): private instance attribute with optional size

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is a negative number
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
