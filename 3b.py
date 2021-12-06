#Advent of code 2021
# 12/04/21 day 3b
# Joe McFarland
# import sys
# import re
import copy

filename = "data3.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#print(a_list)
maxcols = len(a_list[0])

ogen = None
current_list = copy.deepcopy(a_list)
for col in range(maxcols):
    zero_bits = one_bits = 0
    for row in current_list:
        if row[col] == "0":
            zero_bits += 1
        elif row[col] == "1":
            one_bits += 1
    if one_bits >= zero_bits:
        common = 1
    else:
        common = 0
    new_list = []
    for row in current_list:
        if row[col] == str(common):
            new_list.append(row)
    #print(f"new_list(col={col}):\n{new_list}")
    if len(new_list) == 1:
        print(f"found entry, {new_list}")
        #found_ogen = new_list[0]
        ogen = int(new_list[0],2)
        break
    current_list = copy.deepcopy(new_list)
print(f"ogen = {ogen}")

co2 = None
current_list = copy.deepcopy(a_list)
for col in range(maxcols):
    zero_bits = one_bits = 0
    for row in current_list:
        if row[col] == "0":
            zero_bits += 1
        elif row[col] == "1":
            one_bits += 1
    if one_bits < zero_bits:    #### TODO: only diff, refactor into one function
        common = 1      # least common....
    else:
        common = 0
    new_list = []
    for row in current_list:
        if row[col] == str(common):
            new_list.append(row)
    #print(f"new_list(col={col}):\n{new_list}")
    if len(new_list) == 1:
        print(f"found entry, {new_list}")
        #found_co2 = new_list[0]
        co2 = int(new_list[0],2)
        break
    current_list = copy.deepcopy(new_list)
print(f"co2 = {co2}")

print(f"mul = {ogen*co2}")
