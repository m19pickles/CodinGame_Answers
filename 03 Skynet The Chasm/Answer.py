import sys
import math

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

# game loop
while True:
	speed = int(input())  # the motorbike's speed.
	coord_x = int(input())  # the position on the road of the motorbike.
	#check if motorbike is past gap or going to fast
	if coord_x >= road + gap or speed > gap + 1:
		#Slow motorbike
		print("SLOW")
	else:
		#check if jump will cross gap
		if (coord_x + speed) >= (road + gap):
			#jump motorbike
			print("JUMP")
		#check if Speed will get us over gap
		elif speed > gap:
			#wait motorbike as it will make the jump
			print("WAIT")
		else:
			#speed motorbike as it is not going fast enough
			print("SPEED")

