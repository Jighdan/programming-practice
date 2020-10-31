"""
Given two strings, find the number of common characters between them
"""

from string import ascii_lowercase as al

def common_character_count(s1, s2):
	count = 0
	for letter in al:
		temp_1 = s1.count(letter)
		temp_2 = s2.count(letter)
		count += min(temp_1, temp_2)

	return count
