#Advent of code 2021
# 12/01/21 day 1b
# Joe McFarland
# import sys
# import re

filename = "data1.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#print(a_list)

depths = []
for depthstr in a_list:
    depths.append(int(depthstr))
#print(depths)

prev = depths[0]    # skip first entry since no value yet
count_incr = 0
for i, depth in enumerate(depths):
    print(f"{i}, {depth}, {prev}, {count_incr}")
    if i == 0 or i == 1:    # skip first two entries
        continue
    sum = depth + depths[i-1] + depths[i-2]
    print(f"sum={sum}")
    if (i != 2) and (sum > prev):   # dont count first sum since nothing to compare to yet
        count_incr += 1
    prev = sum

print(f"count_incr={count_incr}")
