#!/usr/bin/python3
"""Module to write an empty class Rectangle
"""


class Rectangle:
    """Defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): instance attribute with value of height

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is a negative number
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

    def area(self):
        """Defines logic for finding area

        Returns:
            Integer containing value of area
        """
        area = 0
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Defines logic for finding perimeter

        Returns:
            Integer containing value of perimeter
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return perimeter
        perimeter = 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """Defines str to equal new string of #'s

        Returns:
            New string with no extra newline
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        new_list = []
        if self.__width == 0 or self.__height == 0:
            return ''.join(new_list).rstrip()

        for x in range(0, self.__height):
            for y in range(0, self.__width):
                if type(Rectangle.print_symbol) is list:
                    for x in Rectangle.print_symbol:
                        new_list.append(x)
                new_list.append(Rectangle.print_symbol)
            if x == len(new_list):
                return
            new_list.append('\n')
        return ''.join(new_list).rstrip()

    def __repr__(self):
        """String representation of rectangle to recreate new instances

        Returns:
            string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Defines del to print sentence upon deletion

        Returns:
            Nothing
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Args:
            rect_1: instance of Rectangle
            rect_2: instance of Rectangle

        Raises:
            TypeError: If rect_1 is not an instance of Rectangle
            TypeError: If rect_2 is not an instance of Rectangle

        Returns:
            rect_1 or rect_2 depending on their respective sizes
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
        if rect_1.area() == rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Args:
            cls: instance of Rectangle
            size (int): private instance attribute with optional size

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is negative

        Returns:
            new width and height for Rectangle instance
        """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be >= 0")
        width = size
        height = size
        return cls(width, height)
