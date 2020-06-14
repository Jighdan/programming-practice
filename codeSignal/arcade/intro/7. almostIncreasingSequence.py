"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.
"""

def almost_increasing_sequence(seq):
	dropped = False
	last = prev = min(seq) - 1
	for element in seq:
		if element <= last:
			if dropped:
				return False
			else:
				dropped = True
			if element <= prev:
				prev = last
			elif elm >= prev:
				prev = last = element
		else:
			return True
