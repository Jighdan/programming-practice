"""
Mark first element as sorted
For each unsorted element X
	Extract the element X
	For j <- lastSortedIndex to 0
		if current element j > X
			move sorted element to the right by 1
	insert X here
"""

def insertion_sort(arr):
	key, jndex = [0, 0]
	for index in range(0, len(arr)):
		key = arr[index]
		jndex = index

		while jndex > 0 and arr[jndex - 1] > key:
			arr[jndex] = arr[jndex - 1]
			jndex -= 1

		arr[jndex] = key

	return arr
