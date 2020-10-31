"""
Given an array of integers, print the array elements in reverse order as a
single line of spaced separated numbers.
"""
from typing import List

def print_reverse(array: List[int]) -> None:
    print(" ".join([str(_) for _ in array[::-1]]))
