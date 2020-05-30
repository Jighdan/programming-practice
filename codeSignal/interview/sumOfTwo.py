"""
You have two integer arrays, a and b, and an integer target value v. Determine wheter there is a pair of numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v. Return true if such pair exists, otherwhise return false.
"""

def sumOfTwo(arr_a, arr_b, v):
	complements = [v - num for num in arr_a]
	for num in arr_b:
		if num in complements:
			return True
		else:
			return False
