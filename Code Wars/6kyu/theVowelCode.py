"""
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:
a -> 1 | e -> 2 | i -> 3 | o -> 4 | u -> 5

For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.
"""

def encode(string):
	vowels = {vow: str((list("aeiou").index(vow) + 1)) for vow in list("aeiou")}
	string = list(string)
	for index, letter in enumerate(string):
		if letter in vowels.keys():
			string[index] = vowels[letter]

	return "".join(string)

def decode(string):
	vowels = {str(list("aeiou").index(vowel) + 1): vowel for vowel in list("aeiou")}
	string = list(string)
	for index, letter in enumerate(string):
		if letter in vowels.keys():
			string[index] = vowels[letter]
	return "".join(string)

### Other Solutions ###

def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)