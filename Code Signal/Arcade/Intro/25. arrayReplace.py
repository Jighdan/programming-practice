"""
Given an array of integers, replace all the occurrences of `element_to_replace`
with `substitution_element`.

IN  -> Array<Numbers>, element_to_replace, substitution_element
OUT -> Array<Numbers>

FOR index IN range(0, length_of_array):
    IF array[index] IS EQUAL TO `element_to_replace`:
        SET array[index] AS `substitution_element`
"""

from typing import List

def array_replace(array: List[int], element_to_replace: int,
        substitution_element: int):
    for index in range(0, len(array)):
        if array[index] == element_to_replace:
            array[index] = substitution_element

    return array
