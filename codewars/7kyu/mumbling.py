"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""
    
def accum(mumble):
    mumbles = []
    for index, letter in enumerate(list(mumble)):
        mumbly = letter * (index + 1)
	mumbles.append(mumbly.title())

    return "-".join(mumbles)
