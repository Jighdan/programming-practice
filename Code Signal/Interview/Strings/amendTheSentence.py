"""
You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:

Put a single space between the words.
Convert the uppercase letters to lowercase.
"""

def amendTheSentence(string):
    a = {index: string[index] for index in range(0, len(string))}
    for index in a.keys():
	    if a[index].isupper():
		    requires_space = " " if index != 0 else ""
		    a[index] = f"{requires_space}{a[index].lower()}"
            
    return "".join(a.values())