#Advent of code 2021
# 12/10/21 day 5a
# Joe McFarland
# import sys
# import re
# import copy

#max_x = 10
#max_y = 10
max_x = 1000
max_y = 1000
grid = [[0]*max_x for _ in range(max_y)] 
filename = "data5.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
print(a_list)
#maxcols = len(a_list[0])

# [3, 4] : [1, 4]   # xy1[0] xy1[1] : xy2[0] xy2[1]  : [x1, y1] [x2, y2]
def incrRange(xy1, xy2):
    global grid
    x1 = xy1[0]   
    y1 = xy1[1]   
    x2 = xy2[0]   
    y2 = xy2[1]   
    if x1==x2:
        if y2 > y1:
            start = y1
            end = y2
        else:
            start = y2
            end = y1
        for y in range(start, end+1):
            grid[x1][y] += 1
    elif y1==y2:
        if x2 > x1:
            start = x1
            end = x2
        else:
            start = x2
            end = x1
        for x in range(start, end+1):
            grid[x][y1] += 1
    else:
        print(f"SKIP diag, {line}")

#eg: 0,9 -> 5,9
for line in a_list:
    xy = line.split(" -> ")
    xy1str = xy[0].split(",")
    xy1 = [int(elem) for elem in xy1str]
    xy2str = xy[1].split(",")
    xy2 = [int(elem) for elem in xy2str]
    print(f"{xy1} : {xy2}")
    incrRange(xy1, xy2)

count = 0
for x in range(0, max_x):
    for y in range(0, max_y):
        if grid[x][y] >= 2:
            count += 1

print(f"count = {count}")
