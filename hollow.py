"""
Ulugbek Muslitdinov
umuslitdinov@email.arizona.edu
CSC 110-001

The program consists of three independent functions: hollow_row, hollow_square, hollow_triangle
Each function takes two arguements and creates its own results during processing.
In every function the for loop was used in order to create the resulting string 
"""


def hollow_row(char, N):
    """
    Takes two arguements. Creates the resultng string 'line' with for loop
    returns the reulting string
    """
    line = ""
    for i in range(N):
            if i == 0 or i == N-1:
                line += char
            else:
                line += " "
    return line


def hollow_square(char, N):
    """
    Returns None but prints during execution. Takes 2 arguements
    Has two strings to print: border and inside. Border for first and last row. Inside - for others
    """
    border = char * N
    inside = ""
    for i in range(N):
        if i==0 or i==(N-1):
            inside += char
        else:
            inside += " "
    print(border)
    if N >= 2:
        for i in range(N-2):
            print(inside)
        print(border)


def hollow_triangle(char, N):
    """
    Returns None but prints during execution. Takes 2 arguements
    Uses for loop in for loop to create the shape of triangle
    """
    for i in range(N):
        if i != N-1:
            current_line = ""
            for j in range(i+1):
                if j == 0 or j == i:
                    current_line += char
                else:
                    current_line += " "
            print(current_line)
        else:
            border = char * N
            print(border)


def main():
    hollow_square("@", 1)
    hollow_square("#", 2)
    hollow_square("*", 5)
    hollow_triangle("@", 1)
    hollow_triangle("#", 2)
    hollow_triangle("*", 5)



main()