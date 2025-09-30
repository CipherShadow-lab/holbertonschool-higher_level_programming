#!/usr/bin/python3
"""Defines a class that defines a student by first_name, last_name
and age attributes."""


class Student:
    """A class that defines a Student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns attribute names and values for Student object."""

        if (
            isinstance(attrs, list)
            and all(isinstance(attr, str) for attr in attrs)
        ):
            result = {}
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Updates instance(self) with new values for its attributes."""

        for key, value in json.items():
            setattr(self, key, value)
