"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
"""

def make_array_consecutive2(statues):
	missing_statues = [n for n in range(min(statues), max(statues) + 1) if n not in statues]
	return len(missing_statues)
