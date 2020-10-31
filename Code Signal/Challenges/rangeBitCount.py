"""
You are given two numbers a and b where 0 ≤ a ≤ b. Imagine you construct an array of all the integers from a to b inclusive. You need to count the number of 1s in the binary representations of all the numbers in the array.
"""

def range_bit_count(a, b):
	bit_format = lambda x : "{0:b}".format(x)
	zero_taker = lambda x : x.replace("0", "")
	a_to_b = [bit_format(item) for item in range(a, b + 1)]
	bits = [len(zero_taker(bit)) for bit in a_to_b]
	return sum(bits)
