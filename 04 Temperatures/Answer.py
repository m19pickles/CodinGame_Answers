import sys
import math

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

if len(temps) != 0:
    temps = temps.split()
    abstemps = [abs(int(i)) for i in temps]
    minval = min(abstemps)
    index = [i for i, x in enumerate(abstemps) if x == min(abstemps)]
    ans = temps[index[0]]
    for i in index:
        if len(temps[i]) == 1:
            ans = temps[i]
    print(ans)
else:
    print(0)