#Advent of code 2021
# 12/02/21 day 2b
# Joe McFarland
# import sys
# import re

filename = "data2.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#print(a_list)

depth = 0
hpos = 0
aim = 0
for line in a_list:
    match line.split():
        case "forward", val:
            hpos += int(val)
            depth  += aim*(int(val))
        case "down", val:
            aim += int(val)
        case "up", val:
            aim -= int(val)
        case _:
            print(f"error: {line}")
            exit()
print(f"hpos = {hpos}, depth={depth}, mul = {hpos*depth}")
