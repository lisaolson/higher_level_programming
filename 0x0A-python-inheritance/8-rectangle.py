#!/usr/bin/python3
"""Module to define BaseGeometry Class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Instantiation with width and height
        Args:
            width (int): width as integer value
            height (int): height as integer value
        """
        super().integer_validator("width".format(height), width)
        super().integer_validator("height".format(height), height)
        self.__width = width
        self.__height = height
