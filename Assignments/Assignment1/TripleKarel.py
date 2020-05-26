from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    for i in range(3):
        paint_three_sides()
    turn_left()  # Reversing the Fencepost condition of the last building to face in required direction.

"""
Pre-condition: Karel is at the starting of one of the wall of the rectangle facing the direction in which the wall 
               should be painted.
Post-condition: Karel should paint(place a beeper on) one side of the rectangle without painting the last square where 
                Karel ends and it is not adjacent to the rectangle wall. 
"""
def paint_one_side(): # Karel painting one side of the rectangle. (Step 1)
    while left_is_blocked():
        put_beeper()
        move()

"""
Pre-condition: Karel is at the starting of one of the wall of the rectangle facing the direction in which the wall 
               should be painted.
Post-condition: Karel should paint all three sides of the rectangle, placing beepers on all corners that are adjacent to 
                the wall of the building.
"""
def paint_three_sides(): # Paints all three sides of the rectangle as required. (Step 2)
    for i in range(2):
        paint_one_side()
        turn_90_left()

    paint_one_side()  # Because of Fencepost error condition.
    turn_right()  # For pre-condition and post-condition of paint_three_sides() to match.

"""
Pre-condition: Karel should be in a position that permits it to turn left and move.
Post-condition: Karel facing left and moving one unit ahead to whichever direction Karel was facing previously.
"""
def turn_90_left(): # Turn 90 deg in left direction.
    turn_left()
    move()

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
