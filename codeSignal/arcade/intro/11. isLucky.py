"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.
"""

def is_lucky(n):
	sum_group = lambda lst : sum([int(item) for item in lst])
	n_half_length = int(len(str(n)) / 2)
	first_half, second_half = str(n)[:n_half_length], str(n)[n_half_length:]
	return True if sum_group(first_half) == sum_group(second_half) else False
