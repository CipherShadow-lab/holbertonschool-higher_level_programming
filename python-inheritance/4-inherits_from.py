#!/usr/bin/python3
"""inherits_from Module.
Contains a function that checks if an object is
an instance of an inherited class and not an instance of the
specified class itself.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of an inherited class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
