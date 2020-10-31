"""
Read an integer n. Try to print the following 123...n

... -> represents the values in between.
"""

def print_function(n):
	nums = [str(num) for num in range(1, n + 1)]
	print("".join(nums))
