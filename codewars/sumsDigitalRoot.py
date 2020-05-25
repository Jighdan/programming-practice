"""
A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
"""

def digitalRoot(nums):
    if len(list(str(nums))) > 1:
        string_nums = list(str(nums))
        separated_nums = [int(n) for n in string_nums]
        num_sum = sum(separated_nums)
        return digitalRoot(num_sum)
    else:
        return nums
