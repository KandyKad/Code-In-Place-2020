from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main(): # Main Code
    move_90()
    turn_left()
    move()
    pick_beeper()
    turn_around()
    move()
    move_90()
    turn_karel_right()

"""
Pre-condition: None.
Post-condition: Karel facing right to whichever direction Karel was facing previously.
"""
def turn_karel_right(): # Turn right
    for i in range(3):
        turn_left()

"""
Pre-condition: None. 
Post-condition: Karel facing the opposite direction in whichever direction Karel was facing previously.
"""
def turn_around(): # U-turn
    for i in range(2):
        turn_left()

"""
Pre-condition: None. (I mean Karel should be in a position to move ahead 2 blocks, i.e. front should be clear 2 blocks)
Post-condition: Karel should move 2 blocks ahead in whichever direction it was facing initially. 
"""
def move_ahead(): # Move 2 times
    for i in range(2):
        move()

"""
A move_90() is a kind of movement that a rook does in a game of chess, something like an L-shape.

Pre-condition: Front should be clear for 2 blocks and right should be clear for 1 block.
Post-condition: Karel moves 2 blocks ahead and 1 block right to its initial position and faces the right direction in
                whichever direction it was facing previously.
"""
def move_90(): # Combining the two functions move_ahead() and turn_karel_right() as they are used twice in the code.
    move_ahead()
    turn_karel_right()
    move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
