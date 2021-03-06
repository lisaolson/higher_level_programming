#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """Args:
            size (int): private instance attribute with optional size

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is a negative number
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            value (int): instance attribute with value of size

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is a negative number
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        return value

    def area(self):
        """Defines logic for finding area

        Returns:
            Integer containing value of area
        """
        area = 0
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Defines logic for printing a square

        Returns: None
        """
        if self.__size == 0:
            print()
        for x in range(0, self.__size):
            for y in range(0, self.__size):
                print("#", end="")
            print()
