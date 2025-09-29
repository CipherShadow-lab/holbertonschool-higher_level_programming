#!/usr/bin/python3
"""Defines a function that creates a Python object from a JSON file."""


import json


def load_from_json_file(filename):
    """function creates Python object from JSON file"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
