#!/usr/bin/python3
"""Module to define Square Class
"""
from models.base import Base


class Rectangle(Base):
    """Defines Rectangle, inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation with width, height, x, y, id
        Args:
            id (int): id value as integer
            width (int): width value as integer
            height (int): height value as integer
            x (int): x value as integer initiated with 0
            y (int): y value as integer initiated with 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets value of width
        Args:
            value (int): value as integer
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets value of height
        Args:
            value (int): value as integer
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets value of x
        Args:
            value (int): value as integer
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets value of y
        Args:
            value (int): value as integer
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area
        """
        return (self.__width * self.__height)

    def display(self):
        """Returns print of square
        """
        for b in range(self.__y):
            print()
        for x in range(self.__height):
            for a in range(self.__x):
                print(' ', end="")
            for y in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """Returns formatted string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
               self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        Args:
            *args: sends non-keyworded variable length argument list to fctn
            *kwargs: passes keyworded variable length arguments to fctn
        """
        if args is not None and len(args) > 0:
            for x, y in enumerate(args):
                if x == 0:
                    self.id = y
                if x == 1:
                    self.__width = y
                if x == 2:
                    self.__height = y
                if x == 3:
                    self.__x = y
                if x == 4:
                    self.__y = y
        elif kwargs is not None:
            for x, y in kwargs.items():
                if x == "id":
                    self.id = y
                if x == "width":
                    self.__width = y
                if x == "height":
                    self.__height = y
                if x == "x":
                    self.__x = y
                if x == "y":
                    self.__y = y

    def to_dictionary(self):
        """Returns dictionary representation of a Square
        """
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['width'] = self.width
        new_dict['height'] = self.height
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
