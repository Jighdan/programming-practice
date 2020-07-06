"""
Given a character, check if it represents an odd digit, an even digit or not a digit at all.
"""

def character_parity(symbol):
    is_even = lambda n : n % 2 == 0
    try:
        return "even" if is_even(int(symbol)) else "odd"
    except ValueError:
        return "not a digit"
