#Advent of code 2021
# 12/03/21 day 3a
# Joe McFarland
# import sys
# import re

filename = "data3.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#print(a_list)

# def read_bit(x, pos):
#     mask = 1 << pos
#     return (x & mask) >> pos

def arraytostr(arr):
    mystr = ""
    for col in (arr):
        if col == 0:
            mystr += "0"
        elif col == 1:
            mystr += "1"
        else:
            print(f"ERROR {arr}")
            exit()
    return mystr

maxcols = len(a_list[0])
gamma = [None]*maxcols
epsilon = [None]*maxcols
for col in range(maxcols):   
    zero_bits = one_bits = 0
    for row in a_list:
        if row[col] == "0":
            zero_bits += 1
        elif row[col] == "1":
            one_bits += 1
        else:
            print(f"ERROR {row}")
            exit()
    if zero_bits > one_bits:
        gbit = 0
        ebit = 1
    else:
        gbit = 1
        ebit = 0
    gamma[col] = gbit
    epsilon[col] = ebit

print(f"gamma={gamma}, epsilon={epsilon}") 
g1 = arraytostr(gamma)
e1 = arraytostr(epsilon)
gamma_dec = int(g1,2)
epsilon_dec = int(e1,2)
print(f"gamma_str={g1}, epsilon_str={e1}") 
print(f"gamma_dec={gamma_dec}, epsilon_dec={epsilon_dec}") 
print(f"mul = {gamma_dec*epsilon_dec}")
