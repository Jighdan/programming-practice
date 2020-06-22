"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def shortest_word(string):
    listed = string.split(" ")
    shortest_word = min(listed, key=len)
    return len(shortest_word)

### OTHER SOLUTIONS ###

def find_short(s):
    return min(len(x) for x in s.split())
