#!/usr/bin/python3
"""import module."""


class Square:
    """cerate a class"""

    def __init__(self, size=0):
        """
    constructor.
        Args:
            size: size of sqaure
        """
        self.__size = size
    """
    Area of the square.

    Returns:
        the square area.
    """
    def area(self):
        return self.__size * self.__size
    """
    size of square.

    Returns: the size of square.
    """
    @property
    def size(self):
        return self.__size
    """
    size setter
    Args:
        value: the value set to

    Raises:
        TypeError: size not int
        ValueError: size < 0
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    """
    my_print func that prints

    """
    def my_print(self):
        for i in range(self.__size):
            print()
            for j in range(self.__size):
                print("#", end="")
        print()
