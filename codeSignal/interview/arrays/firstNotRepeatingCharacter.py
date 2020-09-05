"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
"""

from collections import Counter

def first_not_repeating_character(s):
	count = Counter(s).items()
	for i in count:
		if i[1] == 1:
			return i[0]
	return "_"
