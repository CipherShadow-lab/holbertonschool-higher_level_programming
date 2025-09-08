#!/usr/bin/python3

def multiple_returns(sentence):
    result = ""
    i = 0

    if len(sentence) == 0:
        return (0, None)
    else:
        result += sentence[0]
        return (len(sentence), result)
