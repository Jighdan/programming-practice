"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
"""

def sum_multiples_3_and_5(number):
	multiple = lambda x : x % 3 == 0 or x % 5 == 0
	nums = [n for n in range(1, number) if multiple(n)]
	return sum(nums)

### OTHER SOLUTIONS ###
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)