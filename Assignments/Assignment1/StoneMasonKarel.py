from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

def main():
    while front_is_clear():
        repair_one_columnn()
        move_4_steps()
    repair_one_columnn() # For Fencepost error condition, i.e. the last column.

"""
Pre-condition: Karel should be at the bottom of the column to be repaired.
Post-condition: Karel repairs the column required and again comes back to it's initial position in order to move to the
                next column required for repairing.
"""
def repair_one_columnn(): # Karel repairs one column entirely and comes back to initial position.
    turn_left()
    place_missing_arcs()
    turn_around()
    move_ahead()
    turn_left()

"""
Pre-condition: Karel should be at the bottom of the column to be repaired.
Post-condition: Karel repairs(fills the entire column) with beepers, such that every block has only one beeper.
"""
def place_missing_arcs(): # Places beepers at missing positions in the column.
    while front_is_clear():
        if beepers_present(): # As there should not be more than one beeper at any block.
            move()
        else:
            put_beeper()
            move()
    if beepers_present(): # This if and else block is for Fencepost error condition(i.e. for the last block).
        pass # As pass doesn't do anything, it just executes nothing, as given in initial code templates.
    else:
        put_beeper()

"""
Pre-condition: None.
Post-condition: Karel faces opposite direction to whichever direction Karel was facing previously.
"""
def turn_around(): # Karel takes a U-turn, i.e. faces the opposite direction at the same position.
    for i in range(2):
        turn_left()

"""
Pre-condition: None.
Post-condition: Karel moves forward in whichever direction it is facing until it's front is clear.
"""
def move_ahead(): # Moves Karel ahead till its front is clear.
    while front_is_clear():
        move()

"""
Pre-condition: Karel should be in a position to move ahead 4 steps in direction it is facing.
Post-condition: Karel moves ahead 4 steps in whichever direction it is facing initially.
"""
def move_4_steps(): # Moves Karel ahead for 4 steps in whichever direction it is facing.
    for i in range(4):
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
