#!/usr/bin/python3
"""Defines a function that returns a JSON-formatted dictionary representing
the object's attributes. E.g. list, string, integer, boolean"""


import json


def class_to_json(obj):
    """Returns dictionary description of object for JSON serialization"""

    return obj.__dict__
