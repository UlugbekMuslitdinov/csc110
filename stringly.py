"""
Muslitdinov Ulugbek
CSC110/001
EXTRA CREDIT WORK BY TUESDAY
This program contains two functions that will print the triangle from the given string.
"""


def lower_left_triangle(s):
    """
    This function prints the triangle from the given string starting from the top left corner.
    Parameters: s - string
    Output: prints the triangle from the given string.
    """
    count = 1
    while count <= len(s):
        print(s[0:count])
        count = count + 1


def lower_right_triangle(s):
    """
    This function prints the triangle from the given string starting from the top right corner.
    Parameters: s - string
    Output: prints the triangle from the given string.
    """
    count = len(s) - 1
    while count >= 0:
        str_to_print = " " * (len(s) - (len(s) - count))
        str_to_print += s[count:len(s)]
        print(str_to_print)
        count = count - 1


def wordly(word, guess):
    """
    This function checks if the word length is equal to the guess length. If it is not, it returns -1.
    If the word length is equal to the guess length, it loops through the word and compares the letters in guess.
    If the letters are equal in the same place, it adds this letter to result. If the letter is in the guess but in not the same place, it adds a + to result.
    If letter is not in the guess, it adds a space to result.

    Parameters: word - string, guess - string
    Output: result - string
    """
    result = ""
    count = 0
    if len(word) != len(guess):
        return -1
    while count < len(word):
        if word[count] == guess[count]:
            result += word[count]
        elif word[count] in guess:
            result += "+"
        else:
            result += " "
        count += 1
    return result


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
        if s[count] == s[count + 1]:
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
        if s[count] == s[count - 1]:
            return count - 1
        count = count - 1
    return -1


def begins_with(s, prefix):
    """
    This function checks if the given string begins with the given prefix.
    Args:
        s: string
        prefix: string
    Returns:
        True: bool
            or
        False: bool
    """
    if len(s) < len(prefix):
        return False
    count = 0
    while count < len(prefix):
        if s[count] != prefix[count]:
            return False
        count = count + 1
    return True


def ends_with(s, suffix):
    """
    This function checks if the given string ends with the given suffix.
    Args:
        s: string
        suffix: string
    Returns:
        True: bool
            or
        False: bool
    """
    if len(s) < len(suffix):
        return False
    count = len(s) - 1
    while count >= len(s) - len(suffix):
        if s[count] != suffix[count - (len(s) - len(suffix))]:
            return False
        count = count - 1
    return True


def main():
    lower_left_triangle("abcd")
    lower_right_triangle("abcd")


main()
