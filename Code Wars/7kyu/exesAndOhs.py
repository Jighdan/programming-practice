"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
"""

import re
from collections import Counter

def exes_and_ohs(string):
	regex = re.findall("[xo]", string)
        if len(regex) != 0:
            counted = Counter(regex)
            return True if counted.values else False
