"""
Ulugbek Muslitdinov
CSC-110/001
Project 0
There are three functions in this program: square, square_root, and main.
The main function calls the other two functions and prints the results.
"""


def single_row(char, n):
    """
    Returns a single row of a square with n characters.
    """
    return char * n


def print_square(char, n):
    """
    Prints a square with n characters.
    """
    for i in range(n):
        print(single_row(char, n))


def main():
    """
    Main function.
    """
    print_square("@", 3)
    print()
    print_square("#", 2)
    print()
    print_square("*", 5)


main()