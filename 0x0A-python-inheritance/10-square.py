#!/usr/bin/python3
"""Module to define BaseGeometry Class
"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Defines Square that inherits from Rectangle
    """
    def __init__(self, size):
        """Instantiation with size
        Args:
            size (int): size as integer value
        """
        super().integer_validator("size".format(size), size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns area as integer
        """
        return (self.__size * self.__size)
