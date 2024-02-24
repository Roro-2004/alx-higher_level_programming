#!/usr/bin/python3
""" task 2"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """intialize a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width of the rectangle"""
        if (value <= 0):
            raise ValueError("width must be >= 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height of the rectangle"""
        if (value <= 0):
            raise ValueError("height must be >= 0")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            self.__height = value
