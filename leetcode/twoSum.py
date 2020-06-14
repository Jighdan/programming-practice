"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def two_sum(nums, target):
    # a = [[n, k] for n in nums for k in nums if k is not n]
    # for item in a:
    # 	if sum(item) == target:
    # 		first, second = nums.index(item[0]), nums.index(item[-1])
    # 		print(first, second)
    # 		break
    b = {n: nums[n] for n in range(0, len(nums))}
    print(b)
    complements = {n: target - nums[n] for n in range(0, len(nums))}
    print(complements)
    for item in b.items():
    	print(item)



n = [2, 6, 7, 9, 10]
t = 9

def two_sum_two(nums, target):
	complements = [target - n for n in nums]
	print(complements)
	for n in nums:
		if n in complements:
			return nums.index(n)
		else:
			return False

a = two_sum(n, t)
