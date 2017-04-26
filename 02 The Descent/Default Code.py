import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    space_x, space_y = [int(i) for i in input().split()]
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
    print("HOLD")
