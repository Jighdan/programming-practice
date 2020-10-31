"""
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
"""

def square_every_digit(num):
    stringified_squares = [str(int(n) ** 2) for n in list(str(num))]
    new_num = "".join(stringified_squares)
    return int(new_num)
