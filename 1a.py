#Advent of code 2021
# 12/01/21 day 1a
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

prev = depths[0]
count_incr = 0
for depth in depths:
    #print(f"{depth}, {prev}, {count_incr}")
    if depth > prev:
        count_incr += 1
    prev = depth

print(f"count_incr={count_incr}")
