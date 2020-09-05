"""
Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
"""

import re

def dubstep(wubbed_string):
	unwubbed = re.sub("WUB|wub", " ", "wubbed_string")
	return "".join(unwubbed.split())
