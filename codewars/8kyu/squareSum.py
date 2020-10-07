"""
Complete the square sum function so that it squares each number passed into it
and then sums the results together.
"""

def square_sum(numbers: List[float]) -> float:
    return sum([n ** 2 for n in numbers])

