"""
Given the string, check if it is a palindrome.
"""

def check_if_palindrome(word):
	reversed_word = word[::-1]
	if reversed_word == word:
		return True
	else:
		return False
