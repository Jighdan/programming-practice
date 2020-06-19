"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""

def accum(mumble):
	mumbles = []
	for letter in list(mumble):
		mumbly = letter * (list(mumble).index(letter) + 1)
		mumbles.append(mumbly.title())

	return "-".join(mumbles)