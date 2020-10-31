"""
A left rotation operation on an array of size `n` shifts each of the array's elements `1` unit to the left. Given an integer, `d`, rotate the array that many steps left and return the result.
"""

class ListNode:
	def __init__(self, value=0, next=None):
		self.value = value
		self.next = next
		

def array_left_rotation(array, shifts):
	temp = []
	for index in range(0, len(array)):
		temp.append(array[index - shifts])

	return temp

a = [1, 2, 3, 4, 5]

print(array_left_rotation(a, 4))