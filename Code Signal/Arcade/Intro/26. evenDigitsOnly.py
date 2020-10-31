"""
Check if all digits of the given integer are even.

IN  -> Number
OUT -> Boolean

CONVERT num TO String
FOR n IN num:
    CONVERT n TO Number
    IF n % 2 IS NOT EQUAL TO 0:
        RETURN False
RETURN TRUE
"""

def even_digits_only(number: int) -> bool:
    split_number = [int(_) for _ in list(str(number))]
    for num in split_number:
        if num % 2 != 0:
            return False
    return True
