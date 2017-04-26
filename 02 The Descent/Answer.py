import sys
import math

#set initial value for old space craft level
old_space_y = 11
#create empty list for mountains
mountain_h = []
# game loop
while True:
	space_x, space_y = [int(i) for i in input().split()]
	for i in range(8):
		mountain_h.append(int(input()))  # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.

	#check if we have decended to the next pass
	if old_space_y != space_y:
		#set flag for firing being available
		fired = False
		
	#Check if we have already fired this level
	if fired != True:
		#fire if over Highest mountain
		if mountain_h[space_x] == max(mountain_h):
			#print "FIRE" to fire weapons
			print("FIRE")
			#set flag to for firing being Unavailable
			fired = True
		else:
			#print "HOLD" to hold fire
			print("HOLD")
			
	else:
		#print "HOLD" to hold fire
		print("HOLD")
		
	#set new current level to old level
	old_space_y = space_y
	#clears list of mountain Heights
	mountain_h = []