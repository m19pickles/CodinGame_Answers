import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]


if light_y < initial_ty:
        Moves = ["N"]*abs(light_y - initial_ty)
else:
	Moves = ["S"]*abs(light_y - initial_ty)
for i in range(0, abs(light_x - initial_tx)):
        if i >= len(Moves):                        
                if light_x < initial_tx:
                        Moves.append("W")
                else:
                        Moves.append("E")
        else:
                if light_x < initial_tx:
                        Moves[i] = Moves[i] + "W"
                else:
                        Moves[i] = Moves[i] + "E"


# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(Moves.pop(0))
