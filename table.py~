"""
Ulugbek Muslitdinov
umuslitdinov@email.arizona.edu
CSC 110/001

The program consist of 5 functions: repeated, padded, power, print_row and print_table.
 The first function is independent of the others. Other functions call previous functions.
 The aim of the program is to print a table of powers depending on the user input.
"""


def repeated(char, N):
    """
    Returns a string that is N copies of char.
    Function uses while loop to repeat the character and add it to a string variable return_str.
    The function returns the string variable return_str.
    """
    n = 0
    return_str = ""
    while n < N:
        return_str += char
        n += 1
    return return_str


def padded(x, width):
    """
    Returns a string that is width characters long, and is padded with spaces on the left.
    It uses the repeated function to repeat the character and add it to a string variable return_str.
    It also checks if the number length is more than the width. If it is, it returns the number. If it is not, it prints *
    It returns the call of the repeated function with the number and width as arguments.
    """
    x = str(x)
    x_len = len(x)
    if x_len <= width:
        return repeated(" ", width - x_len) + x
    else:
        return repeated("*", width)


def power(base, exponent):
    """
    Returns the value of the base raised to the exponent.
    It checks if the exponent is negative. If it is, it returns -1.
    Else it uses the for loop to raise the base to the exponent.
    It returns the result of the for loop - return_val.
    """
    if exponent < 0:
        return -1
    elif exponent == 0:
        return 1
    else:
        return_val = 1
        for i in range(exponent):
            return_val *= base
        return return_val


def print_row(n, max_power, column_width):
    """
    Returns a string that is the row of the table.
    It uses the padded function to pad the number with spaces.
    It uses the power function to raise the number to the power.
    It uses the for loop to add the results of the power function to a string variable return_str.
    It returns the string variable return_str.
    """
    return_str = ""
    for i in range(max_power):
        return_str += "|"
        return_str += padded(power(n, i+1), column_width)
    return_str += "|"
    print(return_str)


def print_table(max_value, max_power, column_width):
    """
    Returns a string that is the table.
    It uses the print_row function to print the rows.
    It uses the for loop to print the rows.
    It uses the repeated function to print the top and bottom of the table.
    It returns nothing. It prints the table as the function runs.
    """
    upper_border = repeated("-", (column_width + 1) * max_power + 1)
    print(upper_border)
    lower_border = repeated("=", (column_width + 1) * max_power + 1)
    x = 1
    while x <= max_value:
        print_row(x, max_power, column_width)
        x += 1
    print(lower_border)


def main():
    print_table(4, 3, 2)
    print_table(6, 4, 2)


main()
