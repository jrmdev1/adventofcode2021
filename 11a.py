#Advent of code 2021
# 6/22/22 day 11a
# Joe McFarland
# import re

filename = "data11_short2.txt"
#a_list = open(filename).read().splitlines()
a_list = open(filename).read().split()
maxrows = len(a_list)
print(a_list)
maxcols = len(a_list[0])
print(f"maxrows = {maxrows}, maxcols={maxcols}")

array = []

def flash(row, col):
    rcoffset = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
    for offsetsrow, offsetscol in rcoffset:
        r = row+offsetsrow
        c = col+offsetscol
        if r < 0 or r >= maxrows or c < 0 or c >= maxcols:
            print(f"flash exceeded, r={r}, c={c}")
            return

        array[r][c] += 1
        if array[r][c] > 9:
            flash(r, c)
            array[r][c] = 0

def dumpMatrix(octos):
    for y in range(len(octos)):
        for x in range(len(octos[0])):
            print(octos[y][x],end='')
        print()
    print()

for line in a_list:
    row1 = [int(elem) for elem in line]
    #print(f"row={row1}")
    array.append(row1)
print(f"array={array}")

# for row in range(0, maxrows):
#     for col in range(0, maxcols):
#         energy = array[row][col]
#         #print(f"{energy}")

dumpMatrix(array)

for step in range(0, 5):
    for row in range(0, maxrows):
        for col in range(0, maxcols):
            #energy = array[row][col]
            array[row][col] += 1
            if array[row][col] > 9:
                print(f"{row} {col} : exceeded: {array[row][col]}")

                #flash(row, col)

                array[row][col] = 0
            #print(f"{energy}")
    dumpMatrix(array)

#dumpMatrix()
dumpMatrix(array)
    

#print(f"totalrisk = {totalrisk}")