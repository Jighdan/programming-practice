"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.
"""

def abbrev_name(name):
    initials = [n[0].upper() for n in name.split(" ")]
    return ".".join(initials) + "."
