#!/usr/bin/python3
"""MyList Module.
Contains a class MyList that inherits from list
and prints the sorted list.
"""


class MyList(list):
    """Defines the MyList class."""

    def print_sorted(self):
        print(sorted(self))
