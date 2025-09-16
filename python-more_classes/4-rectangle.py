#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class representing rectangle"""

    def __init__(self, width=0, height=0):
        """Initialisation of Instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for __width"""
        return self.__width

    @property
    def height(self):
        """Getter for __height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to return area"""
        return (self.width * self.height)

    def perimeter(self):
        """Method to return perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """Method to print the rectangle"""

        if self.width == 0 or self.height == 0:
            print()
        else:
            # Creating string for printing
            rectangle = ""
            for i in range(self.height - 1):
                rectangle += (self.width * "#" + '\n')
            rectangle += (self.width * "#")
            return rectangle

    def __repr__(self):
        """Method to return a receateable instance"""

        return f"Rectangle({self.width}, {self.height})"
