#!/usr/bin/python3
"""Defines a function that writes a string to a text file
and returns number of characters written"""


def write_file(filename="", text=""):
    """function writes string to utf-8 text file"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
