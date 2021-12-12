#Advent of code 2021
# 12/11/21 day 6a
# Joe McFarland
# import sys
# import re
# import copy

filename = "data6.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
print(a_list)
#maxcols = len(a_list[0])

a_str = a_list[0].split(",")
mylist = [int(elem) for elem in a_str]

numdays = 80

print(f"{mylist}")
for day in range(1, numdays+1):
    for i in range(len(mylist)):
        if mylist[i] == 0:
            mylist[i] = 6
            mylist.append(8)
        else:
            mylist[i] -= 1
    #print(f"{day} : {mylist}")

print(f"total = {len(mylist)}")
