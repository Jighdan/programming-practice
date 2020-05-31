"""
Given an array of integers, write a function that determines whether the array contains any duplicates. Your function should return true if any element appears at least twice in the array, and it should return false if every element is distinct.
"""

def contains_duplicates(a):
	a_set = {n for n in a}
	if len(a_set) != len(a):
		return True
	else:
		return False
