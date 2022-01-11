#Advent of code 2021
# 1/11/22 day 8a
# Joe McFarland
# import sys
# import re
# import copy
filename = "data8.txt"

def isMatch(word):
    # match word:
    #     case "fg":
    match len(word):
        case 2: # num 1
            return True
        case 4: # num 4
            return True
        case 3: # num 7
            return True
        case 7: # num 8
            return True
    return False
            

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#print(a_list)
#maxcols = len(a_list[0])
count = 0
for line in a_list:
    a_str = line.split(" | ")
    sig_str = a_str[0]
    out_str = a_str[1]
    print(f"{sig_str}, {out_str}")
    out_list = out_str.split()
    for word in out_list:
        if isMatch(word):
            count += 1
print(f"count={count}")

