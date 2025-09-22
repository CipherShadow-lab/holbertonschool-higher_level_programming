#!/usr/bin/python3
"""Rectangle Module.
Contains a class Rectangle that inherits
the BaseGeometry class.
"""
from multiprocessing.heap import Arena


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherets BaseGeometry class."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[rectangle] {self.__width}/{self.__height}"
