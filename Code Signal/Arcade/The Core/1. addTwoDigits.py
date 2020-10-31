"""
You are given a two-digit integer n. Return the sum of its digits.
"""

def add_two_digits(n):
	separated_nums = [int(n) for n in list(str(n))]
	return sum(separated_nums)
