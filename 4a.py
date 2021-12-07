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


numboards = int( ((maxrows-2)/6)+1 )
matrix_list = []
print(f"numboards = {numboards}, maxrows={maxrows}")
for boardnum in range( 0, numboards):
    matrix = []
    offset = boardnum*6
    for i in range( 2+offset, 2+offset+5 ):     # was 0,maxrows
        nums = [int(elem) for elem in a_list[i].split()]
        matrix.append( nums )
    print(f"2d:\n{matrix}")
    matrix_list.append(matrix)
print(f"matrix_list:\n{matrix_list}")

#print(f"matrix_list[0]:\n {matrix_list[0]}")
for mat in matrix_list:
    print(f"mat :\n {mat}")
