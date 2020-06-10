"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.
"""

def circle_of_numbers(n, first_number):
	nums= [n for n in range(0, n)]
	mid_index = int(len(nums) / 2)
	first_half = nums[:mid_index]
	second_half = nums[mid_index:]
	if first_number in first_half:
		index = first_half.index(first_number)
		return second_half[index]
	else:
		index = second_half.index(first_number)
		return second_half[index]
