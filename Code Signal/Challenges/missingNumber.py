"""
You are supossed to label a bunch of boxes with numbers from 0 to n, and all the labels are stored in the array arr. Unfortunately one of the labels is missing. Your task is to find it.
"""

def missing_number(arr):
    max_n = max(arr)
    full_arr = [n for n in range(0, max_n)]
    original, full = set(arr), set(full_arr)
    return original - full
