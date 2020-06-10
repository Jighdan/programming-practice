"""
You are given an array of positive ints where every element appears three times, except one that appears only once (let's call it x) and one that appears only twice (let's call it y).
Your task is to find x * x * y.
"""

def missing_value(num_array):
    x = 0
    y = 0
    for num in num_array:
        if (num_array.count(num) == 1):
            x = num
        elif (num_array.count(num) == 2):
            y = num
        else:
            pass
    
    return x * x * y
