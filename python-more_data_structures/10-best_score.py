#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:  # checks is dictionary is None or empty
        return (None)
    highest_score = max(a_dictionary, key=a_dictionary.get)
    return (highest_score)
