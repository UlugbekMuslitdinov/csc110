"""
Muslitdinov Ulugbek
CSC110/001
EXTRA CREDIT WORK FOR PROJECT 5 BY FRIDAY
This program involves functions that are used to create or edit a dictionary.
The exception is a "letter_grade" function that returns a letter grade based on the input of a number grade.
"""


def letter_grade(scope):
    """
    This function returns a letter grade based on the input of a number grade.

    Parameters:
        scope (int): The number grade.

    Returns:
        letter_grade (str): The letter grade.
    """
    if scope >= 90:
        return 'A'
    elif scope >= 80:
        return 'B'
    elif scope >= 70:
        return 'C'
    elif scope >= 60:
        return 'D'
    elif scope >= 50:
        return 'E'
    else:
        return 'F'


def count_vowels(strings):
    """
    This function returns a dictionary with the number of vowels in each string.
    It loops through each string, lowers each letter and counts the number of vowels in each string.

    Parameters:
        strings (list): A list of strings.

    Returns:
        count (dict): A dictionary with the number of vowels in each string.
    """
    count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for word in strings:
        word = word.lower()
        for letter in word:
            if letter in count:
                count[letter] += 1
    return count


def count_words(strings):
    """
    This function returns a dictionary with the number of words in each string.
    It loops through each string, makes from this phrase string the list of words and counts the number of words in each list.

    Parameters:
        strings (list): A list of strings.

    Returns:
        count (dict): A dictionary with the number of words in each string.
    """
    count = {}
    for phrase in strings:
        words = phrase.split()
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    return count


def words_by_first_letter(strings):
    """
    This function returns a dictionary with the number of words starting with each letter.
    It loops through each string and writes the number of words starting with each letter.

    Parameters:
        strings (list): A list of strings.

    Returns:
        count (dict): A dictionary with the number of words starting with each letter.
    """
    count = {}
    for phrase in strings:
        words = phrase.split()
        for word in words:
            if word[0] in count:
                count[word[0]].append(word)
            else:
                count[word[0]] = [word]
    return count


def indices_of_words(strings):
    """
    This function returns a dictionary with the indices of each word in each string.
    It loops through each string and writes the index of the string in which this word is found.

    Parameters:
        strings (list): A list of strings.

    Returns:
        count (dict): A dictionary with the indices of each word in each string.
    """
    count = {}
    for i in range(len(strings)):
        words = strings[i].split()
        for word in words:
            if word in count:
                if i not in count[word]:
                    count[word].append(i)
            else:
                count[word] = [i]
    return count


def by_grade(grades):
    """
    This function returns a dictionary with the names of students in each letter grade.
    It loops through each letter grade and writes the names of students in each letter grade.

    Parameters:
        grades (dict): A dictionary with the names of students and their scores.

    Returns:
        count (dict): A dictionary with the names of students in each letter grade.
    """
    count = {}
    for name in grades:
        if grades[name] in count:
            count[grades[name]].append(name)
        else:
            count[grades[name]] = [name]
    for grade in count:
        count[grade].sort()
    return count


def compute_letter_grades(grades):
    """
    This function returns a dictionary with the names of students as keys and their letter grades as values.
    It loops through each name, calculates the grade letter using "letter_grade" function and writes the letter grade of each student.

    Parameters:
        grades (dict): A dictionary with the names of students and their scores.

    Returns:
        count (dict): A dictionary with the names of students as keys and their letter grades as values.
    """
    count = {}
    for name in grades:
        average = 0
        for score in grades[name]:
            average += score
        average /= len(grades[name])
        letter_score = letter_grade(average)
        count[name] = letter_score
    return count


def add_letter_grade(grades):
    """
    This function returns a dictionary with the names of students as keys and their letter grades for each section as values.
    If the section is not in the dictionary, it adds it with the value of 0.

    Parameters:
        grades (dict): A dictionary with the names of students and their scores.

    Returns:
        count (dict): A dictionary with the names of students as keys and their letter grades for each section as values.
    """
    for name in grades:
        if "test" not in grades[name]:
            grades[name]["test"] = 0
        if "hw" not in grades[name]:
            grades[name]["hw"] = 0
        average_score = (2*grades[name]["test"] + grades[name]["hw"]) / 3
        letter_score = letter_grade(average_score)
        grades[name]["course"] = letter_score
    return grades


def compute_all_letter_grades(grades):
    """
    This function returns a dictionary with the names of students as keys and their letter grades as values.
    It loops through each name, calculates the grade letter using "letter_grade" function and writes the letter grade of each student.

    Parameters:
        grades (dict): A dictionary with the names of students and their scores.

    Returns:
        count (dict): A dictionary with the names of students as keys and their letter grades as values.
    """
    letter_scores = {}
    for name in grades["test"]:
        test_score = grades["test"][name]
        if name in grades["hw"]:
            hw_score = grades["hw"][name]
        else:
            hw_score = 0
        average_score = (2*test_score + hw_score) / 3
        letter_score = letter_grade(average_score)
        letter_scores[name] = letter_score
    for name in grades["hw"]:
        if name not in letter_scores:
            test_score = 0
            hw_score = grades["hw"][name]
            average_score = (2*test_score + hw_score) / 3
            print(average_score)
            letter_score = letter_grade(average_score)
            letter_scores[name] = letter_score
    return letter_scores


def unflatten_grades(grades):
    """
    This function returns a dictionary with the names of students as keys and their scores for each section as values.
    It loops through each name, calculates the grade letter using "letter_grade" function and writes the letter grade of each student.

    Parameters:
        grades (dict): A dictionary with the names of students and their scores.

    Returns:
        unflatten (dict): A dictionary with the names of students as keys and their scores for each section as values.
    """
    unflatten = {}
    for dictionary in grades:
        if dictionary["name"] in unflatten:
            if dictionary["category"] in unflatten[dictionary["name"]]:
                unflatten[dictionary["name"]][dictionary["category"]].append(dictionary["score"])
            else:
                unflatten[dictionary["name"]][dictionary["category"]] = [dictionary["score"]]
        else:
            unflatten[dictionary["name"]] = {}
            unflatten[dictionary["name"]][dictionary["category"]] = [dictionary["score"]]
    return unflatten


def gather(values):
    """
    This function loops through the list and adds the numbers that come after the letter as the values of this letter.
    It will add the values to this letter until it reaches another letter.

    Parameters:
        values (list): A list of numbers and letters.

    Returns:
        count (dict): A dictionary with the names of students as keys and their scores for each section as values.
    """
    count = {}
    last_str = None
    for value in values:
        if isinstance(value, str):
            last_str = value
            if value not in count:
                count[value] = []
        else:
            if last_str is not None:
                if last_str in count:
                    count[last_str].append(value)
                else:
                    count[last_str] = [value]
    return count
