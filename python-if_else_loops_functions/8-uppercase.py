#!/usr/bin/python3
def uppercase(str):
    result = ""
    for character in str:
        if 'a' <= character <= 'z':
            uppercase_char = chr(ord(character) - 32)
            result += uppercase_char
        else:
            result += character
    print(result)
