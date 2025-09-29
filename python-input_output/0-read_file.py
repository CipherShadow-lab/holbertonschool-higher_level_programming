#!/usr/bin/python3
"""Defines a function that reads a text file and prints to stdout"""

def read_file(filename=""):
    """function reads and prints a utf-8 text file"""

    with open(filename, "r", encode="utf-8") as f:
        content = filename.read()
        print(content, end="")
