from karel.stanfordkarel import *

# Makes a line  of slope 1/2.
def main():
    put_beeper()
    while front_is_clear():
        make_line_of_slope_half()


# There is no need to edit code beyond this point

def make_line_of_slope_half():
    if (front_is_clear()):
        turn_left()
        move()
        turn_right()
    for i in range(2):
        if front_is_blocked():
            break
        else:
            move()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program()