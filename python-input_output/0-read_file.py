#!/usr/bin/python3
"""Defines a function that reads a text file and prints to stdout"""

def read_file(filename=""):
    """function reads, prints and returns a utf-8 text file"""

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
        return content
