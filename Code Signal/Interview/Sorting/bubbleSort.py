"""
Given an array of integers, sort it.
"""

def bubble_sort(arr):
	def swap(firstIndex, secondIndex):
		temp = arr[firstIndex]
		arr[firstIndex] = arr[secondIndex]
		arr[secondIndex] = temp

	for item in range(len(arr)):
		j = 0
		stop = len(arr) - item
		while j < stop - 1:
			if arr[j] > arr[j + 1]:
				swap(j, j + 1)
			j += 1

	return arr
