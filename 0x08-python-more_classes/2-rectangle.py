#!/usr/bin/python3
"""This is a Rectangle Class"""


class Rectangle:
    """A Rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor for Rectangle
           Takes two values to intiate the width and height
           Attributes:
                width   width value of the rectangle
                height  height value of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """A getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter for the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """A getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter for the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calc the area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """calc the premiter"""
        if(self.__height == 0 or self.__width == 0):
            return 0
        else:
            return ((self.__height + self.__width) * 2)
