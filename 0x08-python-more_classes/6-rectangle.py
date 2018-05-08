#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
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
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return value

    def area(self):
        area = 0
        area = self.__width * self.__height
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        perimeter = 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        new_list = []
        if self.__width == 0 or self.__height == 0:
            return ''.join(new_list).rstrip()

        for x in range(0, self.__height):
            for y in range(0, self.__width):
                new_list.append("#")
            if x == len(new_list):
                return
            new_list.append('\n')
        return ''.join(new_list).rstrip()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

