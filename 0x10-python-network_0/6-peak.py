#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers: A list of integers.

    Returns:
        The value of a peak in the list, or None if the list is empty or None.
    """

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    lo = 0
    hi = len(list_of_integers) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return list_of_integers[lo]
