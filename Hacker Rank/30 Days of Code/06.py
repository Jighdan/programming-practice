"""
Given a string of an unknown length, return its even-indexed and odd-indexed characters as  space-separated strings on a single line.
"""

def even_split(word):
	is_even = lambda n : n % 2 == 0
	indexes = [index for index in range(0, len(word))]
	even_letters = [word[index] for index in indexes if is_even(index) == True]
	odd_letters = [word[index] for index in indexes if is_even(index) == False]
	split_word = "{} {}".format("".join(even_letters), "".join(odd_letters))
	return split_word