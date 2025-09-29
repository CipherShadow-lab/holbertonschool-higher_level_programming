#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file
and returns number of characters added"""


def append_write(filename="", text=""):
    """function appends a string to a (utf-8) text file"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
