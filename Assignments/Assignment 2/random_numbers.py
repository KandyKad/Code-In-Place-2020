"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

"""
In this program we define 3 constants: 
NUM_RANDOM - Which determines the number of random numbers to be printed.
MIN_RANDOM - The minimal value of the random numbers to be generated (inclusive).
MAX_RANDOM - The maximal value of the random numbers to be generated (inclusive).

We define a for loop which iterates over NUM_RANDOM and prints that many numbers.
In the print command, a function random.randint() with arguments MIN_RANDOM, MAX_RANDOM generates 
random numbers with the range [MIN_RANDOM, MAX_RANDOM] both inclusive. 
"""
import random

NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100

def main():

    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM,MAX_RANDOM))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
