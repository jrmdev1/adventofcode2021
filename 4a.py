#Advent of code 2021
# 12/06/21 day 4a
# Joe McFarland
# import sys
# import re
import copy

filename = "data4_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
print(a_list)
#maxcols = len(a_list[0])

draw_strings = a_list[0].split(",")
draws = [int(elem) for elem in draw_strings]
print(f"\ndraws={draws}")

#make 2d array (list of lists)
matrix = []
for i in range( 2, 2+5 ):     # was 0,maxrows
    nums = [int(elem) for elem in a_list[i].split()]
    matrix.append( nums )
print(f"2d:\n{matrix}")

#print(f"mul = {ogen*co2}")