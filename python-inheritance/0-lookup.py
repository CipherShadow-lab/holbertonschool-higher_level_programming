#!/usr/bin/python3
"""Lookup module.

Contains a function that returns a list of
available attributes and attributes of an object
"""


def lookup(obj):
    """Returns list of attributes and methods of an object"""
    return dir(obj)
