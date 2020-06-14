"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
"""

from collections import Counter

def count_number_of_duplicates(s):
	dups = [i for i in Counter(s.lower()).items() if i[1] > 1]
	return len(dups)
