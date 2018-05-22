#!/usr/bin/python3

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            for x,y in enumerate(args):
                if x == 0:
                    self.id = y
                if x == 1:
                    self.size = y
                if x == 2:
                    self.x = y
                if x == 3:
                    self.y = y

        elif kwargs is not None:
            for x,y in kwargs.items():
                if x == "id":
                    self.id = y
                if x == "width":
                    self.size = y
                if x == "x":
                    self.x = y
                if x == "y":
                    self.y = y

    def to_dictionary(self):
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['size'] = self.size
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict        
