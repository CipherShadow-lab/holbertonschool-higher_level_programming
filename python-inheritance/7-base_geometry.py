#!/usr/bin/python3
"""base_geometry Module.
Contains a class called BaseGeometry.
"""


class BaseGeometry():
    """Defined class called BaseGeometry"""
    def area(self):
        """Method raises Exception of area not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validates that the value is an integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
