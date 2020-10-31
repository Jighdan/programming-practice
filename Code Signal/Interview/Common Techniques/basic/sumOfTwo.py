"""
You have two integer arrays, a and b, and an integer target value v. Determine wheter there is a pair of numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v. Return true if such pair exists, otherwhise return false.
"""

def sum_of_two(a, b, v):
	complements = {v - num for num in a}
	result = {num for num in b if num in complements}
	return True if len(result) >= 1 else False
