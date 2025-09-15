#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """
    This class defines a square by its size.
    """

    def __init__(self, size):
        """
        Initialises the square with a specific size.
        The size is a private attribute.
        """
        self.__size = size
