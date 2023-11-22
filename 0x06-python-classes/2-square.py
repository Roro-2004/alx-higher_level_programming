#!/usr/bin/python3
"""import module."""


class Square:
    """cerate a class"""

    def __init__(self, size=0):
        """
    constructor.
        Args:
            size: size of sqaure

        Raises:

            TypeError: size not int
            ValueError: size < 0
            """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >=0')
        self.__size = size
