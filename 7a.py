#Advent of code 2021
# 12/20/21 day 7a
# Joe McFarland
# import sys
# import re
# import copy

filename = "data7.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
print(a_list)
#maxcols = len(a_list[0])
a_str = a_list[0].split(",")
mylist = [int(elem) for elem in a_str]

maxpos = max(mylist)
print(f"maxpos={maxpos}")

print(f"{mylist}")

lowest_fuel = 10000000
#lowest_pos = maxpos
for hpos in range(1,maxpos+1):
    per_pos_fuel = 0
    for crab_pos in mylist:
        fuelcost = max(crab_pos, hpos) - min(crab_pos, hpos)
        #print(f"hpos: {hpos}, crab_pos: {crab_pos}, fuelcost: {fuelcost}")
        per_pos_fuel += fuelcost
    if per_pos_fuel < lowest_fuel:
        lowest_fuel = per_pos_fuel
        lowest_pos = hpos
        print(f"updated low(pos,fuel): {lowest_pos}, {lowest_fuel}")
    #print(f"hpos {hpos}, per_pos_fuel {per_pos_fuel}")
print(f"lowest_pos = {lowest_pos}, lowest_fuel = {lowest_fuel}")
