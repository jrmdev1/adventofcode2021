#Advent of code 2021
# 12/11/21 day 6a
# Joe McFarland
# import sys
# import re
# import copy

filename = "data6_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
print(a_list)
#maxcols = len(a_list[0])

a_str = a_list[0].split(",")
mylist = [int(elem) for elem in a_str]

print(f"{mylist}")
