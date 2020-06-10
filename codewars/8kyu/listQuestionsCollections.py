"""
I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements. I'll appreciate for your help.
"""

def array_plus_array(arr1, arr2):
	return sum(arr1) + sum(arr2)

"""
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
"""

def count_sheeps(sheep):
	return sheep.count(True)

"""
In this kata you will create a function that takes in a list and returns a list with the reverse order.
"""

def reverse_list(arr):
	return arr[::-1]

"""
Write a method sum that takes an array of numbers and returns the sum of the numbers. These may be integers or decimals for Ruby and any instance of Num for Haskell. The numbers can also be negative. If the array does not contain any numbers then you should return 0.
"""

def sum_array(arr):
	return sum(arr)

"""
Given an array of integers your solution should find the smallest integer.
"""

def smallest_num(arr):
	return min(arr)

"""
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!
"""

def better_than_average(class_points, your_score):
	avg = sum(class_points) / len(class_points)
	return True if your_score > avg else False

"""
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:
"""

def find_needle(arr):
	index = str(arr.index("needle"))
	return "found the needle at position {}".format(index)

"""
Your task is to make two functions, max and min (maximum and minimum in PHP and Python) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.
"""

def minimum_arr(arr):
	return min(arr)

def maximum_arr(arr):
	return max(arr)