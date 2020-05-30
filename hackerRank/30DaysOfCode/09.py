
"""
Write a factorial function that takes a positive integer, N as a parameter and returns the result of N! (N factorial)
"""
import numpy as np

def factorial(num):
	if num == 1:
		return num
	else:
		fact = [n for n in range(1, num + 1)]
		return np.prod(fact)