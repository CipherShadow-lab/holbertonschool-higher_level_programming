#!/usr/bin/python3
"""
This module defines the text_indentation function
"""


def text_indentation(text):
    """ Function that prints indented text.
    Args:
        text (str): text to print
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    length = len(text)

    while i < length:
        print(text[i], end="")

        if text[i] in ['.', '?', ':']:
            print("\n")

            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue

        i += 1
