#Advent of code 2021
# 12/02/21 day 2b
# Joe McFarland
# import sys
# import re

filename = "data2_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#print(a_list)

depth = 0
hpos = 0
for line in a_list:
    match line.split():
    #cmd_val = line.split(" ")
    #val = int(cmd_val[1])
        case "forward", val:
            hpos += int(val)
        case "down", val:
            depth += int(val)
        case "up", val:
            depth -= int(val)
        case _:
            print(f"error: {line}")
            exit()
print(f"hpos = {hpos}, depth={depth}, mul = {hpos*depth}")
