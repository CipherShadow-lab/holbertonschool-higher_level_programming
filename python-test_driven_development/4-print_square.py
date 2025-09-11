#!/usr/bin/python3
def print_square(size):
    """ Function that prints a square.
    Args:
        size (int): size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for sym in range(size):
        print("#" * size)

