#!/usr/bin/python3
"""is_same_class Module.
Contains a function that returns True if object is
exactly an instance of the specified class.
Otherwise returns False.
"""

def is_same_class(obj, a_class):
    """Checks if an object is exaclty an instance of a class."""
    return type(obj) is a_class
