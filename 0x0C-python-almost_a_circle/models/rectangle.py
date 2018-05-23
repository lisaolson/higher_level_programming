#!/usr/bin/python3
"""
module defines rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    class defines Rectangle:
    args:
        width (int): width
        height (int): height
        x (int): x
        y (int): y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer method
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        getter returns the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter for rectangle
        Args:
        value (int): width of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter returns the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter for rectangle
        Args:
        value (int): height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        getter returns the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter for rectangle
        Args:
        value (int): x of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter returns the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter for rectangle
        Args:
        value (int): y of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method that calculates and returns the area
        Returns:
            int: The area.
        """
        return self.width * self.height

    def display(self):
        """prints the rectangle with the # character
        """
        for row0 in range(self.y):
            print()
        for row in range(self.height):
            for column0 in range(self.x):
                print(" ", end="")
            for column in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns id x/y - width/height
        """
        return ("[Rectangle] " + "(" + str(self.id) +
                ") " + str(self.x) + "/" + str(self.y) +
                " - " + str(self.width) + "/" +
                str(self.height))

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute
        Args:
            *args: list of arguments
            **kwargs: keyword dictionary of arguments
        """
        list = ["id", "width", "height", "x", "y"]
        count = 0
        if args:
            for arg in args:
                count += 1
                if count == 1:
                    self.id = arg
                elif count == 2:
                    self.width = arg
                elif count == 3:
                    self.height = arg
                elif count == 4:
                    self.x = arg
                elif count == 5:
                    self.y = arg
        elif kwargs:
            for key, value in kwargs.items():
                if key in list:
                    setattr(self, key, value)
                    """
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.__width = value
                    elif key == "height":
                        self.__height = value
                    elif key == "x":
                        self.__x = value
                    elif key == "y":
                        self.__y = value
                    """

    def to_dictionary(self):
        """returns dictionary representation of a Rectangle
        """
        dictionary = dict(self.__dict__)
        for key in dictionary:
            new_key = key.replace("_Rectangle__", "")
            dictionary[new_key] = dictionary.pop(key)
        return dictionary
        """
       new_dict = {'id': self.id, 'x': self.x, 'y': self.y,
        'width': self.width, 'height': self.height}
       return new_dict
