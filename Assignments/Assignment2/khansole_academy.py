"""
File: khansole_academy.py
-------------------------
#Comments
Here we created 3 constants:
1. LOWER_RANGE: Lower limit of the numbers to be given for addition.
2. UPPER_RANGE: Upper limit of the numbers to be given for addition.
3. CONSECUTIVE_CORRECT_ANSWER: Number of correct answers so that the user passes the test.

An initial counter, 'correct_answer_count' is initialized to 0 so that it starts to count the consecutive correct
answers. A while() loop is used so that the until the consecutive correct answer is not equal to 3, the program will
keep on asking questions to the user. 2 random numbers 'num1' and 'num2' are created using the function,
'random.randint()'. A question asking the sum of both the numbers is asked to the user. The answer of the sum of
both the numbers is taken as an input from the user.

>> If the answer is correct, a validation msg is given to the user and the counter of the correctness is increased by 1.
>> If the answer is incorrect, a msg regarding the same and giving the right answer is displayed to the user.
>> This process is repeated till the user answers 3 questions correctly in a row. (while loop)
>> After that a msg appreciating the user is displayed.
"""

import random

LOWER_RANGE = 10
UPPER_RANGE = 99
CONSECUTIVE_CORRECT_ANSWERS = 3

def main():

    correct_answer_count = 0   # Initial initializer for the count of correct answer.

    while (correct_answer_count < CONSECUTIVE_CORRECT_ANSWERS):
        num1 = random.randint(LOWER_RANGE, UPPER_RANGE)  # Random number 1
        num2 = random.randint(LOWER_RANGE, UPPER_RANGE)  # Random number 2

        print("What is " + str(num1) + " + " + str(num2) + "?")
        answer = int(input("Your answer: "))  # User input

        if(answer == num1 + num2):
            correct_answer_count += 1
            print("Correct! You've gotten " + str(correct_answer_count) + " correct in a row.")

        else:
            correct_answer_count = 0   # If wrong answer, then the correct answer count should be initialized to 0.
            print("Incorrect. The expected answer is " + str(num1+num2))

    # Obviously this line will be printed after while loop is exited i.e. after the count reaches for 3 (here)
    # consecutive correctly answered questions.
    print("Congratulations! You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
