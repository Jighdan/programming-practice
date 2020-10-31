"""
Given a divisor and a bound, find the largest integer N such that:

N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
It is guaranteed that such a number exists.
"""

def max_multiple(divisor, bound):
	divs = [n for n in range(1, bound + 1) if n % divisor == 0]
	return max(divs)
