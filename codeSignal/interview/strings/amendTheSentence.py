"""
You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:

Put a single space between the words.
Convert the uppercase letters to lowercase.
"""

import re

def amend_the_sentence(s):
	pass

string = "HelloWorldOH"
a = re.findall("[A-Z]", string)
b = [string.index(i) for i in a]

d = list(string)
