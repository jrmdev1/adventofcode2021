#Advent of code 2021
# 1/15/22 day 9a
# Joe McFarland
# import sys
# import re
# import copy
filename = "data9.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#print(a_list)
maxcols = len(a_list[0])
print(f"maxrows = {maxrows}, maxcols={maxcols}")

array = []
for line in a_list:
    row1 = [int(elem) for elem in line]
    #print(f"row={row1}")
    array.append(row1)
#print(f"array={array}")

totalrisk = 0
for row in range(0, maxrows):
    for col in range(0, maxcols):
        height = array[row][col]
        rcoffset = [[0,-1], [-1,0], [1,0], [0,1]]
        flag = 0
        for roff, coff in rcoffset:
            #print(f"{roff}, {coff}")
            rcheck = row + roff
            ccheck = col + coff
            if rcheck >= 0 and rcheck < maxrows and ccheck >= 0 and ccheck < maxcols:
                if height < array[rcheck][ccheck]:
                    flag += 1
            else:
                flag += 1
            if flag == 4:
                print(f"low point: {row}, {col}")
                totalrisk += (height + 1)

print(f"totalrisk = {totalrisk}")
