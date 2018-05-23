#!/usr/bin/python3
"""Module to define Square Class
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines Square, inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation with size, x, y, id
        Args:
            id (int): id value as integer
            size (int): size value as integer
            x (int): x value as integer initiated with 0
            y (int): y value as integer initiated with 0
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns formatted string
        """

        strr = "[Square] ({}) {}/{} - {}"
        return strr.format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Returns size
        """

        return self.width

    @size.setter
    def size(self, value):
        """Sets values of width, height and size
        Args:
            value (int): value as integer
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        Args:
            *args: sends non-keyworded variable
            *kwargs: passes keyworded variable length
        """

        if args is not None and len(args) > 0:
            for x, y in enumerate(args):
                if x == 0:
                    self.id = y
                if x == 1:
                    self.size = y
                if x == 2:
                    self.x = y
                if x == 3:
                    self.y = y

        if kwargs is not None:
            for x, y in kwargs.items():
                if x == "id":
                    self.id = y
                if x == "size":
                    self.width = y
                if x == "x":
                    self.x = y
                if x == "y":
                    self.y = y

    def to_dictionary(self):
        """Returns dictionary representation of a Square
        """

        new_dict = {}
        new_dict['id'] = self.id
        new_dict['size'] = self.size
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
