from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

"""
---------------------------- LOGIC ----------------------------
In this code, Karel puts beepers alternately from both the sides until the entire row is filled with beepers. After 
that, it puts an extra beeper on the middle corner. Then Karel moves to any one of the end points and picks the beepers
of the entire row, again alternatively from both sides. As there are two beepers on the centre corner, after picking up 
all the beepers, effectively there will be one beeper present at the centre corner if it is an odd-sided world. For 
worlds of even side, Karel puts a beeper at the end as all beepers get picked up in the above process. No commands other
than the basic Karel commands and conditions used in this program.
"""
def main():

    put_beepers_on_end_points() # Put one beeper on both the end points.

    while(no_beepers_present()):   # To complete the entire filling up of the row. If this while() block is not
        put_beeper_alternately() # present, and only put_beepers_alternately() is present, it will put beepers
                                   # only on two opposite ends of the row, other middle blocks i.e effectively the
                                   # middle block will be without a beeper.

    put_extra_beeper_on_the_centre_corner() # Put one extra beeper at the centre of the row.

    pick_beepers_from_end_points() # Pick one beeper from both the end points.

    if(front_is_clear()):
        while(beepers_present()):       # The while loop logic is similar to the above while loop.
            pick_beeper_alternately() # Picks up beepers alternatively from both the end points.

    odd_even_world_size_equalling() # For even sized world all beepers get picked up so 1 extra beeper needs to be put.

"""
Pre-condition: None.
Post-condition: It equalizes the required condition of Karel to be on a beeper at the midpoint for odd or even world.
"""
def odd_even_world_size_equalling(): # If odd world, do nothing; if even world place a beeper for size of world > 2.
    round_about()
    if beepers_present(): # This (if block) is executed for ODD LENGTH OF WORLD, i.e after picking beepers up, Karel
        pass              # ends up on the required(middle) beeper only.

    else:                       # This (else block) is executed for EVEN LENGTH OF WORLD, because it picks all beepers.

        if front_is_blocked():  # This (if block) is specially for world of (2 * N), as it has wall nearer to it and to
            round_about()       # lay beeper on only one of the middle corner(either 1st or 2nd).
        else:
            put_beeper()        # This (else block) is for all even worlds greater than 2*2, as in even world Karel ends
                                # up at any one of the middle corner but picking all the beepers laid so one beeper
                                # should be put.

"""
Pre-condition: None.
Post-condition: Karel puts one extra beeper on the centre corner.
"""
def put_extra_beeper_on_the_centre_corner():
    round_about()      # The put_beeper() before move_ahead() in the function is for placing 2 beepers on the middle
    put_beeper()       # corner, so that when all beepers are picked up, there would be effectively one beeper on the
    move_ahead()       # centre corner.
    turn_around()

"""
Pre-condition: None
Post-condition: Karel puts one beeper on both the end points of the row and takes a U-turn.
"""
def put_beepers_on_end_points(): # Put beepers on end-points of the row.
    put_beeper()
    move_ahead()
    put_beeper()
    round_about()

"""
Pre-condition: There should be at least one beeper on both the end-points of the row.
Post-condition: Karel picks one beeper from both the end points of the row and takes a U-turn.  
"""
def pick_beepers_from_end_points(): # Pick beepers from the end-points of the row.
    pick_beeper()
    move_ahead()
    pick_beeper()
    round_about()

"""
Pre-condition: No beepers should be present on the initial starting block.
Post-condition: Karel puts beepers in a row alternatively for each end only once. To use this function to fill up the 
                entire row, include this function in a while loop as written in the main func.
"""
def put_beeper_alternately(): # Karel puts beepers alternately from either side only once.
    while no_beepers_present():
        move()
    round_about() # For pre and post condition of put_beeper_alternatively() to be valid, when in a while loop.
    put_beeper()
    move()

"""
Pre-condition: Beepers should be present at then initial starting block.
Post-condition: Karel picks beepers in a row alternatively for each end only once. To use this function to pick beepers
                from the entire row, include this function in a while loop as written in the main func.
"""
def pick_beeper_alternately(): # Karel picks beepers alternatively from either side only once.
    while beepers_present():
        move()
    round_about() # For pre and post condition of pick_beeper_alternatively() to be valid, when in a while loop.
    pick_beeper()
    move()

"""
Pre-condition: None.
Post-condition: Karel faces opposite direction to whichever direction Karel was facing previously.
"""
def turn_around(): # Turn Karel in opposite direction at the same position.
    for i in range(2):
        turn_left()

"""
Pre-condition: Karel should be in a position to move 1 block backwards.
Post-condition: Karel takes a U-turn and moves one block forward.(i.e. effectively one block backwards)
"""
def round_about(): # Take a U-turn and move 1 block ahead if possible.
    turn_around()
    if front_is_clear():
        move()

"""
Pre-condition: None
Post-condition: Karel moves ahead in the initial direction it is facing, as long as its front is clear.
"""
def move_ahead(): # Move till front is clear.
    while front_is_clear():
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
