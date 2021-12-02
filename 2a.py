#Advent of code 2021
# 12/02/21 day 2a
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
for line in a_list:
    cmd_val = line.split(" ")
    val = int(cmd_val[1])
    if cmd_val[0] == "forward":
        hpos += val
    elif cmd_val[0] == "down":
        depth += val
    elif cmd_val[0] == "up":
        depth -= val
    else:
        print("error: {cmd_val}")
        exit()

print(f"hpos = {hpos}, depth={depth}, mul = {hpos*depth}")
