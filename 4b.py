#Advent of code 2021
# 12/07/21 day 4b
# Joe McFarland
# import sys
# import re
# import copy

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

#make list of 2d arrays (list of lists of lists)
numboards = int( ((maxrows-2)/6)+1 )
matrix_list = []
called_list = []
print(f"numboards = {numboards}, maxrows={maxrows}")
for boardnum in range( 0, numboards):
    matrix = []
    called = []
    offset = boardnum*6
    for i in range( 2+offset, 2+offset+5 ):
        nums = [int(elem) for elem in a_list[i].split()]
        called_nums = [False for elem in a_list[i].split()]
        matrix.append( nums )
        called.append( called_nums )
    print(f"2d:\n{matrix}")
    matrix_list.append(matrix)
    called_list.append(called)
print(f"matrix_list:\n{matrix_list}")
#print(f"called_list:\n{called_list}")

#print(f"matrix_list[0]:\n {matrix_list[0]}")
#for mat in matrix_list:
#    print(f"mat :\n {mat}")

def calcScore( boardnum ):
    score = 0
    for row in range(0,5):
        for col in range(0,5):
            if called_list[boardnum][row][col] != True:
                score += matrix_list[boardnum][row][col]
    return score

# def dumpBoard( boardnum ):
#     for row in range(0,5):
#         for col in range(0,5):
#             val = matrix_list[boardnum][row][col]
#             if called_list[boardnum][row][col] == True:
#                 Called = "C"
#             else:
#                 Called = ""
#             print(f"{val}{Called}, ")

def isWin( boardnum, draw):
    for row in range(0,5):
        count = 0
        for col in range(0,5):
            if called_list[boardnum][row][col] == True:
                count += 1
                if count >= 5:
                    score = calcScore( boardnum )
                    print(f"Score = {score}, draw={draw}, finalscore={score*draw}")
                    return True
    for col in range(0,5):
        count = 0
        for row in range(0,5):
            if called_list[boardnum][row][col] == True:
                count += 1
                if count >= 5:
                    score = calcScore( boardnum )
                    print(f"Score = {score}, draw={draw}, finalscore={score*draw}")
                    return True

for draw in draws:
    for boardnum in range( numboards ):
        for row in range(0, 5):
            for col in range(0, 5):
                if matrix_list[boardnum][row][col] == draw:
                    called_list[boardnum][row][col] = True
                    if( isWin(boardnum, draw) ):
                        print(f"WIN found, boardnum {boardnum+1}")
                        #dumpBoard(boardnum)
                        #print(f"matrix_list\n{matrix_list}")
                        exit()
