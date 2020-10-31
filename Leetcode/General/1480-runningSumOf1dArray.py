"""
Given an array `nums`. We define a running sum as an array as
`runningSum[i] = sum(nums[0]...nums[i])`.

Return the running sum of sums
"""

def running_sum(nums):
	for index in range(1, len(nums)):
		nums[index] = nums[index - 1] + nums[index]

	return nums
