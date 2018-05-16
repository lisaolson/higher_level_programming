#!/usr/bin/python3
"""Module to define BaseGeometry Class
"""


class BaseGeometry:
    """Defines BaseGeometry
    """

    def area(self):
        """Raises Exception if not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integers

        Args:
            name (str): name of class
            value (int): value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def area(self):
        """Returns area as integer
        """
        return (self.__width * self.__height)

    def __str__(self):
        """Returns string of name with width / height
        """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


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
