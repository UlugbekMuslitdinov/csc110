"""
Ulugbek Muslitdinov
umuslitdinov@email.arizona.edu
CSC 110-001

This program consists of 11 independent functions that are not connected with each other.
"""


def second_largest(numbers):
    """
    This function returns the second-largest number in a numbers.
    The function loops through the numbers and finds the largest number.
    The function then loops through the numbers again and finds the second-largest number.

    Params:
        numbers: a numbers of numbers

    Returns:
        second_lar: integer
    """
    large = 0
    for i in range(len(numbers)):
        if large < numbers[i]:
            large = numbers[i]
    second_largest = 0
    for i in range(len(numbers)):
        if second_largest < numbers[i]:
            if numbers[i] != large:
                second_largest = numbers[i]
    return second_largest


def between(numbers, lower, upper):
    """
    This function returns a numbers of numbers that are between the lower and upper bounds.
    The function loops through the numbers and finds the numbers that are between the lower and upper bounds.

    Params:
        numbers: a numbers of numbers
        lower: an integer - the lower bound
        upper: an integer - the upper bound

    Returns:
        between_list: a numbers of numbers
    """
    between_list = []
    for i in numbers:
        if lower <= i <= upper:
            between_list.append(i)
    return between_list


def no_duplicates(numbers):
    """
    This function returns a numbers of numbers that do not have duplicates.
    The function loops through the numbers and adds the numbers to a numbers that are not currently in the numbers.

    Params:
        numbers: a numbers of numbers

    Returns:
        no_duplicates_list: a numbers of numbers
    """
    no_duplicates_list = []
    for i in numbers:
        if i not in no_duplicates_list:
            no_duplicates_list.append(i)
    return no_duplicates_list


def del_duplicate_adjacents(numbers):
    """
    This function returns a numbers of numbers that do not have adjacent duplicates.
    The function deletes adjacent duplicates from the numbers and returns the numbers.

    Params:
        numbers: a numbers of numbers

    Returns:
        numbers: the original edited numbers
    """
    i = 1
    n = len(numbers)
    while i < n:
        if numbers[i] == numbers[i - 1]:
            del numbers[i]
            n -= 1
        else:
            i += 1


def sum_sublists(lists):
    """
    This function returns the sum of the sublists in numbers of lists.
    The function loops through the numbers of lists and adds the sublist values sum to a numbers.

    Params:
        lists: a numbers of lists

    Returns:
        sum_list: a numbers of numbers
    """
    sums = []
    for list in lists:
        sum = 0
        for i in list:
            sum += i
        sums.append(sum)
    return sums


def flatten(lists):
    """
    This function returns a numbers of numbers that are in the numbers of lists.
    The function loops through the numbers of lists and adds the sublist values to a numbers.

    Params:
        lists: a numbers of lists

    Returns:
        flattened_list: a numbers of numbers
    """
    flat_list = []
    for list in lists:
        for i in list:
            flat_list.append(i)
    return flat_list


def is_median(numbers, target):
    """
    This function returns True if the target is the median of the numbers.
    The function loops through the numbers and counts the number of greater and smaller numbers than the target.

    Params:
        numbers: a numbers of numbers
        target: an integer

    Returns:
        True or False
    """
    above = 0
    below = 0
    equal = 0
    for i in numbers:
        if i > target:
            above += 1
        elif i < target:
            below += 1
        else:
            equal += 1
    z = below - above
    if z >= 0:
        return equal >= z
    else:
        return equal >= -z


def differences(numbers):
    """
    This function returns a numbers of the differences between adjacent numbers in the numbers.
    The function loops through the numbers and adds the difference between current and next values of numbers adjacent numbers to a numbers.

    Params:
        numbers: a numbers of numbers

    Returns:
        differences_list: a numbers of numbers
    """
    differences_list = []
    for i in range(len(numbers) - 1):
        differences_list.append(numbers[i + 1] - numbers[i])
    return differences_list


def odds_or_evens(numbers):
    """
    This function returns a numbers of the odd or even numbers in the numbers.
    The function loops through the numbers and adds the odd or even numbers to a numbers and compares number of values in each numbers.
    Then the function returns the numbers with the most values.

    Params:
        numbers: a numbers of numbers

    Returns:
        odd_even_list: a numbers of numbers
    """
    odds = []
    evens = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(odds) > len(evens):
        return odds
    else:
        return evens


def running_total(numbers):
    """
    This function returns a numbers of the running total of the numbers in the numbers.
    The function loops through the numbers and adds the current value to the previous value in the numbers.

    Params:
        numbers: a numbers of numbers

    Returns:
        running_total_list: a numbers of numbers
    """
    running_total_list = []
    sum = 0
    for i in numbers:
        sum += i
        running_total_list.append(sum)
    return running_total_list


def comma_separated(numbers) -> str:
    """
    This function returns a string of the numbers in the numbers separated by commas.
    The function loops through the numbers and adds the values to the string separated by commas.

    Params:
        numbers: a numbers of numbers

    Returns:
        comma_separated_string: a string
    """
    comma_separated_list = ""
    count = 0
    while count < len(numbers):
        comma_separated_list += str(numbers[count])
        count += 1
        if count < len(numbers):
            comma_separated_list += ", "
    return comma_separated_list

