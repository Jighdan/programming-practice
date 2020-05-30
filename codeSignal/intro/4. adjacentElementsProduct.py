"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
"""

def adjacent_elements_product(arr):
	products = []
	for item in range(0, len(arr) - 1):
		product = arr[item] * arr[item + 1]
		products.append(product)

	return max(products)
