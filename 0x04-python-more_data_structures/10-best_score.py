#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) pr len(a_dictionary) == 0:
        return None
    return max(a_dictionary.keys())
