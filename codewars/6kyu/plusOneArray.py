"""
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

	- The array can't be empty
	- Only non-negative, single digit integers are allowed

Return null for invalid inputs.
"""

def plus_one_array(arr):
	if len(arr) == 0:
		return None

	stringed = [str(n) for n in arr if n >= 0 & n <= 9]

	if len(arr) != len(stringed):
		return None

	adder = int("".join(stringed)) + 1
	composed = [int(n) for n in list(str(adder))]
	return composed
