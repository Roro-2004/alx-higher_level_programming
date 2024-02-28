#!/usr/bin/python3
"""This is a Rectangle Class"""


class Rectangle:
    """A Rectangle
       Arguments:
               number_of_instances var that counts the no of objects
               print_symbol var that stores a rep for the rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor for Rectangle
           Takes two values to intiate the width and height
           Attributes:
                width   width value of the rectangle
                height  height value of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if ((self.__height == 0) or (self.__width == 0)):
            return 0
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        """prints the representation of rectangle"""
        strr = ""
        if (self.__height != 0 and self.__width != 0):
            for i in range(self.__height):
                for j in range(self.__width):
                    if isinstance(self.print_symbol, int):
                        strr += str(self.print_symbol)
                    else:
                        strr += self.print_symbol
                if (i != self.__height - 1):
                    strr += "\n"
        return strr

    def __repr__(self):
        """print the rectangle format"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print bye to deleted rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        elif (rect_2.area() > rect_1.area()):
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns the form of rectangle's square"""
        return cls(size, size)
