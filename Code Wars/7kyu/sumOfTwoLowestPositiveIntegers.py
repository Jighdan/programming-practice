"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
"""

def sum_two_smallest_numers(numbers):
    sorted_nums = sorted(numbers)
    return sorted_nums[0] + sorted_nums[1]
