"""
Simple transposition is a basic and simple cryptography technique. We make 2 rows and put the first a letter in Row 1, the second in the Row 2, third in Row 1 and so on until the end. Then we put the text from Row 2 next to the Row 1 text and that's it.

Complete the function that receives a string and encrypt it with this simple transposition.
"""

def simple_transposition(text):
    is_even = lambda n : n % 2 == 0
    listed, indexed = list(text), range(0, len(text))
    row_1 = [listed[n] for n in indexed if is_even(n)]
    row_2 = [listed[n] for n in indexed if not is_even(n)]
    transposed = "{}{}".format("".join(row_1), "".join(row_2))
    return transposed


### Other Solutions ###

def simple_transposition(text):
    text_1 = text[0::2]
    text_2 = text[1::2]
    return text_1 + text_2
