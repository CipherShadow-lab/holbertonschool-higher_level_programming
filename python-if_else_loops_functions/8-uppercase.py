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


        
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")