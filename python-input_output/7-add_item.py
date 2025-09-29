#!/usr/bin/python3
"""Defines a script that adds all arguments to a Python list
and then saves them to a file."""


import sys
import os
import json


def save_to_json_file(my_obj, filename):
    """function writes Python object to a text file using JSON representation"""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """function creates Python object from JSON file"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

filename = "add_item.json"  # filename used for saving

if os.path.exists(filename):  # try loading existing list from file
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])  # add new arguments - skipping script name

save_to_json_file(items, filename)  # save updated list
