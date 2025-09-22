#!/usr/bin/python3
"""is_kind_of_class Module.
Contains a function that returns True if object is
an instance of the specified class or subclass of that class.
Otherwise returns False.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
