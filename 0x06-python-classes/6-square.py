#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
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
        self.size = size
        self.position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Args:
            value (int): instance attribute with value of size

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is a negative number
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        if value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value
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
            return
        if self.__position[0] >= 0 and self.__position[1] >= 0:
            for j in range(0, self.__position[1]):
                print()
        for x in range(0, self.__size):
            for i in range(0, self.__position[0]):
                print(" ", end="")
            for y in range(0, self.__size):
                print("#", end="")
            print()
