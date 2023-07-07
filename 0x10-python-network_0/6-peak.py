#!/usr/bin/python3
"""Finds a peak in a list of unsorted INTs"""


def find_peak(list_of_integers):
    """Finds a peak"""

    if list_of_integers is None or list_of_integers == []:
        return None
    hi = len(list_of_integers)
    mid = int(hi // 2)
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
