"""
You are supposed to label a bunch of boxes with numbers from 0 to n, and all the labels are stored in the array arr. Unfortunately one of the labels is missing. Your task is to find it.
"""

def missing_number(arr):
	for i in range(0, len(arr) + 1):
		if i not in arr:
			return i
			