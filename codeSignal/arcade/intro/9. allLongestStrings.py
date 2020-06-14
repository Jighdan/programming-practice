"""
Given an array of strings, return another array containing all of its longest strings.
"""

def allLongestStrings(arr):
    sort_array = sorted(arr, key=len, reverse=True)
    longest = [s for s in sort_array if len(s) >= len(sort_array[0])]
    return longest
