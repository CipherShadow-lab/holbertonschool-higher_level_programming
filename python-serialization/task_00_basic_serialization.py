#!/usr/bin/python3
"""This creates a basic serialization module that adds
functionality to serialize a Python dictionary to a JSON file
and deserialize the JSON file to recreate the Python dictionary."""


import json


def serialize_and_save_to_file(data, filename):
    """Method serializes a Python dictionary to a JSON file"""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Method returns a Python dictionary with deserialized JSON data."""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
