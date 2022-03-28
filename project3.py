"""
Muslitdinov Ulugbek
CSC110/001
EXTRA CREDIT WORK BY MONDAY
This program has two functions that find repetition in a given string.
 First function finds the first repetition, while another function finds the last repetition.
"""


def first_repetition(s):
    """
    This function finds the first repetition in a given string.
    Args:
        s: string
    Returns:
        index: int
            or
        -1: int
    """
    count = 0
    while count < len(s) - 1:
        if s[count] == s[count+1]:
            return count
        count = count + 1
    return -1


def last_repetition(s):
    """
    This function finds the last repetition in a given string.
    Args:
        s: string
    Returns:
        index: int
            or
        -1: int
    """
    count = len(s) - 1
    while count >= 0:
        if s[count] == s[count-1]:
            return count - 1
        count = count - 1
    return -1
