#!/usr/bin/python3
import sys

if __name__ == "__main__":

    args = sys.argv[1:]  # excludes progam/script name
    count = len(args)

    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
