"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

"""
This program prints the liftoff count of a spaceship 10,9,...,2,1 and then 'Liftoff!'.
A For() loop is used in the program with a constant LIFT_OFF_COUNT as a counting parameter for the for() loop.
As the count is in reverse order starting from 10, we print the difference between the range value and the 
iterable variable 'i' as i starts from 0. Hence, (LIFT_OFF_COUNT - i). At last we print the string "Liftoff!".
"""
LIFT_OFF_COUNT = 10

def main():
    for i in range(LIFT_OFF_COUNT):
        print(LIFT_OFF_COUNT - i)

    print("Liftoff!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
