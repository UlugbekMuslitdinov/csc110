"""
Muslitdinov Ulugbek
CSC110/001
EXTRA CREDIT WORK BY TUESDAY
This program contains two functions that handle operations with dictionaries, lists and sets.
"""


def sum_two(D1, D2):
    """
    This function takes two dictionaries and returns a new dictionary that contains the sum of the values of the two if the keys are the same.

    Params:
        D1: a dictionary
        D2: a dictionary

    Returns:
        result: a dictionary that contains the sum of the values of the two if the keys are the same.
    """
    result = {}
    for key in D1:
        if key not in result:
            result[key] = 0
        result[key] += D1[key]
    for key in D2:
        if key not in result:
            result[key] = 0
        result[key] += D2[key]
    return result

# print(sum_two({}, {"a": 1}))
# assert sum_two({}, {}) == {}
# assert sum_two({}, {"a": 1}) == {"a": 1}
# assert sum_two({"a": 1}, {}) == {"a": 1}
# assert sum_two({"a": 1}, {"a": 2}) == {"a": 3}
# assert sum_two({"a": 1}, {"a": 2, "b": 3}) == {"a": 3, "b": 3}


def sum_all(list_dictionaries):
    """
    This function takes a list of dictionaries and returns a new dictionary that contains the sum of the values of the dictionaries with the same keys.

    Params:
        list_dictionaries: a list of dictionaries

    Returns:
        result: a dictionary that contains the sum of the values of the dictionaries with the same keys.
    """
    result = {}
    for dictionary in list_dictionaries:
        for key in dictionary:
            if key in result:
                result[key] += dictionary[key]
            else:
                result[key] = dictionary[key]
    return result


def two_grams(words):
    """
    This function takes a list of words and returns a dictionary with the number of times each two adjacent words occur in the list starting from the first word.

    Params:
        words: a list of words

    Returns:
        result: a dictionary with the number of times each two adjacent words occur in the list starting from the first word.
    """
    result = {}
    for i in range(len(words) - 1):
        pair = (words[i].lower(), words[i + 1].lower())
        if pair in result:
            result[pair] += 1
        else:
            result[pair] = 1
    return result


def keep_first(dictionaries):
    """
    This function takes a list of dictionaries and create the dictionary with the set of first and last names as key, and GPA as value.

    Params:
        dictionaries: a list of dictionaries

    Returns:
        result: a dictionary with the set of first and last names as key, and GPA as value.
    """
    result = {}
    for dictionary in dictionaries:
        if "GPA" in dictionary:
            first_last = dictionary["First Name"], dictionary["Last Name"]
            if first_last not in result:
                grade = dictionary["GPA"]
                result[first_last] = grade
    return result


def merge_ascending(L1, L2):
    """
    This function takes two lists and returns a new list that contains the elements of the two lists in ascending order.
    It compares the values of the same index of the two lists and adds the smaller value and then the larger value to the new list.

    Params:
        L1: a list
        L2: a list

    Returns:
        result: a list that contains the elements of the two lists in ascending order.
    """
    result = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1
    while i < len(L1):
        result.append(L1[i])
        i += 1
    while j < len(L2):
        result.append(L2[j])
        j += 1
    return result



def start_longest_run(numbers):
    """
    This function takes a list of numbers and returns the starting index of the longest run of numbers in the list.

    Params:
        numbers: a list of numbers

    Returns:
        result: the starting index of the longest run of numbers in the list.
    """
    index_of_first_run = 0
    current_index = 0
    current_count = 0
    max_count = 0
    if len(numbers) == 0:
        return -1
    for i in range(len(numbers)):
        if numbers[i] == numbers[current_index]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                index_of_first_run = current_index
            current_index = i
            current_count = 1
    if current_count > max_count:
        max_count = current_count
        index_of_first_run = current_index
    return index_of_first_run



def mode(numbers):
    """
    This function takes a list of numbers and returns one of them, which occurs most often in the list.
    If there are multiple numbers that occur most often, return the smallest one.

    Params:
        numbers: a list of numbers

    Returns:
        result: one of the numbers that occurs most often in the list.
    """
    result = {}
    if len(numbers) == 0:
        return None
    for index in range(len(numbers)):
        if numbers[index] not in result:
            result[numbers[index]] = []
        result[numbers[index]].append(index)
    max_count = 0
    max_num_len = 0
    for num in result:
        if len(result[num]) > max_num_len:
            max_num_len = len(result[num])
            max_count = num
        elif len(result[num]) == max_num_len:
            if num < max_count:
                max_count = num
    return max_count
