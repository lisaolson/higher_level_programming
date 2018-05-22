#!/usr/bin/python3



import sys
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        for b in range(self.__y):
            print()
        for x in range(self.__height):
            for a in range(self.__x):
                print(' ', end="")
            for y in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            for x,y in enumerate(args):
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
            for x,y in kwargs.items():
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
        
