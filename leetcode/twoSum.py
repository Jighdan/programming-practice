"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def two_sum(nums, target):
	nums_list = [n for n in nums if n <= target]
	nums_sums = [[num1, num2] for num1 in num_list for num2 in num_list if num_list.index(num2) != num_list.index(num1)]
	valid_sums = []
	for possible_sum in nums_sums:
		if (sum(possible_sum) == target):
			num1_index = nums.index(possible_sum[0])
			num2_index = nums.index(possible_sum[-1])
			valid_sums.append([num1_index, num2_index])
			break
		else:
			pass

	return valid_sums