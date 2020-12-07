"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""

"""
In this program 2 variables are defined 'num1' and 'num2', which store the values input by the user.
The values are taken as float values(real numbers) by the command 'float(input("Enter the req. number: "))'.
A new variable 'result' calculates the difference b/w num1 and num2 by '-(negation)' operator and stores it in it.
Finally the result of the subtraction is printed by the print command with the result variable type-casted to a string.
"""

def main():

    print("This program subtracts one number from another.")

    num1 = float(input("Enter first number: ")) #Input 1
    num2 = float(input("Enter second number: ")) #Input 2

    result = num1 - num2 #Result calculation

    print("The result is " + str(result)) #Return statement


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
