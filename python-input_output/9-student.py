#!/usr/bin/python3
"""Defines a class that defines a student by first_name, last_name
and age attributes."""


class Student:
    """A class that defines a Student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of a Student."""

        return self.__dict__
