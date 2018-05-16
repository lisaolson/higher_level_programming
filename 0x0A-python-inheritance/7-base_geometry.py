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
