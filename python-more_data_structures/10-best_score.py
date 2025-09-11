#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:  # checks is dictionary is None
        return (None)
    highest_score = max(a_dictionary, key=a_dictionary.get)
    return (highest_score)
