#!/usr/bin/python3
"""Module to define get and set the width and height
"""


class Rectangle:
    """Defines a Rectangle
    """

    def __init__(self, width=0, height=0):
        """Args:
            width (int): private instance attribute with optional width
            height (int): private instance attribute with optional height

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is a negative number
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): instance attribute with value of width

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is a negative number
        """
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): instance attribute with value of height

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is a negative number
        """
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return value
