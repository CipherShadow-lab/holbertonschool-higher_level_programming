#!/usr/bin/python3
"""Sqaure Module.
Contains a class Square that inherits
the Rectangle class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherets Rectangle class."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
    