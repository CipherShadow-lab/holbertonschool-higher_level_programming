#!/usr/bin/python3

def read_file(filename=""):
    """function reads a text file and prints to stdout"""

    with open(filename, "r", encode="utf-8") as f:
        content = filename.read()
        print(content, end="")
