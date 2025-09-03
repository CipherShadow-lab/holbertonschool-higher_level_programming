#!/usr/bin/python3
def islower(c):
    ascii_val = ord(c)
    if ascii_val in range(97, 123):
        return True
    else:
        return False
