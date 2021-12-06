#Advent of code 2021
# 12/03/21 day 3b
# Joe McFarland
# import sys
# import re
import copy

filename = "data3_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
print(a_list)

# def read_bit(x, pos):
#     mask = 1 << pos
#     return (x & mask) >> pos

# def arraytostr(arr):
#     mystr = ""
#     for colval in (arr):
#         if colval == 0:
#             mystr += "0"
#         elif colval == 1:
#             mystr += "1"
#         else:
#             print(f"ERROR {arr}")
#             exit()
#     return mystr

maxcols = len(a_list[0])

ogen = c02 = None
current_list = copy.deepcopy(a_list)
for col in range(maxcols):
    zero_bits = one_bits = 0
    #col = 0
    for row in current_list:
        if row[col] == "0":
            zero_bits += 1
        elif row[col] == "1":
            one_bits += 1
    if one_bits >= zero_bits:
        most_common = 1
    else:
        most_common = 0
    #col = 0
    new_list = []
    for row in current_list:
        if row[col] == str(most_common):
            new_list.append(row)
    print(f"new_list(col={col}):\n{new_list}")
    if len(new_list) == 1:
        print(f"found entry, {new_list}")
        #found_ogen = new_list[0]
        ogen = int(new_list[0],2)
        break
    current_list = copy.deepcopy(new_list)
print(f"ogen = {ogen}")

# print(f"gamma={gamma}, epsilon={epsilon}") 
# g1 = arraytostr(gamma)
# e1 = arraytostr(epsilon)
# gamma_dec = int(g1,2)
# epsilon_dec = int(e1,2)
# print(f"gamma_str={g1}, epsilon_str={e1}") 
# print(f"gamma_dec={gamma_dec}, epsilon_dec={epsilon_dec}") 
# print(f"mul = {gamma_dec*epsilon_dec}")
