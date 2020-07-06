"""
Your task is to make a function that can take any non-negative integer as a argument and return it with it's digits in descending order.
"""

def descending_orders(num):
    nums = [n for n in list(str(num))]
    nums.sort(reverse=True)
    return int("".join(nums))
