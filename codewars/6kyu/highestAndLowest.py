"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
"""

"""
nums <-- split and convert the items in the string to integers
sorted_nums <-- sort nums
hi, lo <-- sorted_nums indexed
"""

def high_and_low(string_of_numbers):
	nums = [int(num) for num in string_of_numbers.split(" ")]
	nums.sort()
	highest, lowest = str(max(nums)), str(min(nums))
	return " ".join([highest, lowest])

###################
# Other Solutions #
###################

def high_and_low(numbers):
    n = map(int, numbers.split(' '))
    return "{} {}".format(max(n), min(n))