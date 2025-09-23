#!/usr/bin/python3

class VerboseList(list):
    """Prints notification messages when an item is added."""

    def append(self, item):
        """Adds an item to the end of the list and prints notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list and prints notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Removes first occurence of item and prints notification."""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """Removes and returns item at index and prints notification."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
