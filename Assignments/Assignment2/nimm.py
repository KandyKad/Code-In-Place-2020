"""
File: nimm.py
-------------------------
Here we have defined only 1 constant:
1. TOTAL_STONES: No. of stones initially present to play the Game of Nimm.

Variables:
1. stone_left: Number of stones left before each players turn (Initially referenced from global variable TOTAL_STONES).
2. chance: Variable that controls which players chance would be next.
3. stone: The number of stone/s picked by each player during his turn.

Initially the 'stone_left' and 'chance' variable are defined accordingly. A while() loop is iterated until,
the no. of stones left is 0. The chance variable decides which player's turn would be next. A print statement
prints the number of stones left at that player's turn to be picked up. The input demands the user to pick up
either 1 or 2 stones from the remaining number of stones.

>> The while() loop after the input statement determines that the input taken from the user is either 1 or 2.
>> print() after the while statement prints an extra blank line so that the terminal looks neat and readable.
>> The chance variable is modified accordingly so that other player's chance occurs at the next iteration.
>> 'stone_left' is decremented accordingly to the number of stones picked by the user in that iteration.

Lastly since the chance variable is modified depending upon who picked the stone at the last, so it is used to
determine the winner in the if-else() block at the end of the code.
"""

TOTAL_STONES = 20

def main():
    stone_left = TOTAL_STONES  # Initial stones count.
    chance = 0  # Variable changing players turn alternately.

    while(stone_left > 0):  # Loop till all the stones are picked by the players.

        if(chance == 0):  # Player 1 chance.

            print("There are " + str(stone_left) + " stones left")

            stone = int(input("Player 1 would you like to remove 1 or 2 stones? "))  # Initial user input

            while(stone < 1 or stone > 2):
                stone = int(input("Please enter 1 or 2: "))  # If user enters other than 1 or 2
            print()  # For that extra space between each player's turn

            chance += 1  # Alternate the chance
            stone_left -= stone  # So that stone count is decreased every time a player picks up stones

        else:  # (chance == 1) Player 2 chance

            print("There are " + str(stone_left) + " stones left")

            stone = int(input("Player 2 would you like to remove 1 or 2 stones? "))  # Initial user input

            while(stone < 1 or stone > 2):
                stone = int(input("Please enter 1 or 2: "))  # If user enters other than 1 or 2
            print()  # For that extra space between each player's turn

            chance -= 1  # Alternate the chance
            stone_left -= stone  # So that stone count is decreased every time a player picks up stones

    if(chance == 0):
        print("Player 1 wins!")
    elif(chance == 1):
        print("Player 2 wins!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
