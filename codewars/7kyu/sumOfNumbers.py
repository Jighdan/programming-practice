"""
Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
"""

def sum_of_numbers(num_1, num_2):
	if num_1 != num_2:
		ADDER = 1 if num_2 >= 0 else -1
		nums_list = range(num_1, num_2 + ADDER)
		return sum(nums_list)
	return num_1