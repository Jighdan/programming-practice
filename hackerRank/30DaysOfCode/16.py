"""
Read a string and print it's integer value, if the string cannot be converted to an integer print "Bad String"
"""

def convert_to_integer(text):
	try:
		return int(text)
	except ValueError:
		return "Bad String"