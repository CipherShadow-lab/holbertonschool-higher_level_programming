#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class representing rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialisation of Instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod  # behaves like a regular function
    def bigger_or_equal(rect_1, rect_2):
        """Returns biggest rectangle. Otherwise rect_1 if both are equal."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def __str__(self):
        """Sets print behaviour of Rectangle object"""
        rectangle = ""

        if self.width > 0 and self.height > 0:
            for i in range(self.height):
                rectangle += str(self.print_symbol) * self.width + '\n'

            return rectangle[:-1]

    def __repr__(self):
        """Method to return a repeatable instance"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Method deletes an instance of a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
