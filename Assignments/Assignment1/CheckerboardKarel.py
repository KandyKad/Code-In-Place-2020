from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

"""
---------------------------- LOGIC ----------------------------
In this code, Karel puts beepers alternately in each column. For odd columns, going_up() function performs the task.
And for even columns, coming_down() function performs the task. Both the functions maintain the pre conditions of the 
other functions respectively. 2 Corner Cases, i.e. (1 * n) & (n * 1) worlds are encountered. They can be solved by 
applying simple constrains. No commands other than the basic Karel commands and conditions used in this program.
"""
def main():

    if(front_is_clear()):         # For all worlds except (1 * n).

        turn_left()               # So that precondition of going_up matches initially.

        while(front_is_clear()):  # For all worlds except (1 * n) & (n * 1). [CORNER CASES]
            going_up()
            coming_down()

        turn_right()
        if(front_is_clear()):    # For (n * 1) worlds, as after turning left initially, their front would be blocked.
            put_beeper_alternately()

    else:                        # For (1 * n) worlds, as their front would be blocked initially itself.
        turn_left()
        put_beeper_alternately()

"""
Pre-condition: Karel should be at the bottom level to perform the going_up function.
Post-condition: Performs the filling of odd column in up direction, and also aligns Karel to fill the next column with 
                required pre/post conditions.
"""
def going_up():
    check_beeper()
    put_beeper_alternately()
    check_beeper_upgoing()

"""
Pre-condition: Karel should be at the top level to perform the coming_down function.
Post-condition: Performs the filling of even column in down direction, and also aligns Karel to fill the next column 
                with required pre/post conditions.
"""
def coming_down():
    check_beeper()
    put_beeper_alternately()
    check_beeper_downcoming()

"""
Pre-condition: None.
Post-condition: Puts beepers alternately in a line, till front is clear.
"""
def put_beeper_alternately():
    while (front_is_clear()):
        move()
        put_beeper()
        if (front_is_clear()):
            move()

"""
Pre-condition: None.
Post-condition: Checks if beepers present at the given block. If yes, then moves one block forward if front is clear.
                Else, stays at the same block.
"""
def check_beeper():
    if(beepers_present()):
        if(front_is_clear()):
            move()

"""
Pre-condition: After placing beepers alternately, the beeper should be at the top level of the checker-board.
Post-condition: Takes a right turn and aligns Karel for filling next column if front is clear. Also checks if previous 
                block(before taking right turn) was filled or not. If filled, it leaves the next block blank. If it   
                wasn't filled, then fills the block in the next column.
"""
def check_beeper_upgoing():
    turn_right()
    if(front_is_clear()):
        if(beepers_present()):
            move()
            turn_right()
        else:
            move()
            turn_right()
            put_beeper()  # Placing beeper when last block of previous column is not filled.

"""
Pre-condition: After placing beepers alternately, the beeper should be at the bottom level of the checker-board.
Post-condition: Takes a left turn and aligns Karel for filling next column if front is clear. Also checks if previous 
                block(before taking left turn) was filled or not. If filled, it leaves the next block blank. If it   
                wasn't filled, then fills the block in the next column.
"""
def check_beeper_downcoming():
    turn_left()
    if(front_is_clear()):
        if(beepers_present()):
            move()
            turn_left()

        else:
            move()
            turn_left()
            put_beeper()  # Placing beeper when last block of previous column is not filled.

"""
Pre-condition: None.
Post-condition: Karel facing right to whichever direction Karel was facing previously.
"""
def turn_right(): # Turns Karel right
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
