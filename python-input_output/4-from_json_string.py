#!/usr/bin/python3
"""Defines a function that returns an object (data structure) represented
by a JSON string."""


import json


def from_json_string(my_str):
    """function converts JSON string to Python object"""

    return json.loads(my_str)
