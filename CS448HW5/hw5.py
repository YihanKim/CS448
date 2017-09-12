# CS448 Assignment #5

# 25 Apr 2017
# 20130143 Yihan Kim
# Python 3.4


# ----------
# 0. Purpose
# 0.1 Complete the XOR Disribution Table(XDT) of S4 box in DES.
# 0.2 Complete the Linear Distribution Table(LDT) of S5 box in DES.
# ----------


# ----------
# 1. Constant

# 1.1 S4_box : listof(listof(int))
# describing S4_box information
# each number is accessible by using S4[i][j],
# where 0 <= i < 4 and 0 <= j < 16.

S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]];

# 1.1 S5_box : listof(listof(int))
# describing S5_box

S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]];
# ----------


# ----------
# 2. Functions

# 2.1 i2b : (integer, integer) |-> integer
def i2b(x: int, k: int):
        # return string of binary correspondence of integer
        # with fixed length k
        # if binary length of x is less than k,
        # the first and following blank bit will be filled with 0

        assert 0 <= x < 2 ** k
        return ('0' * k + bin(x)[2:])[-k:]

# 2.2 get_s4 : integer |-> integer
def get_s4(x: int):
        # read x(6-bit integer) and find correspond index in S4 box
        # first index: b1b6 (b6 is MSB of x)
        # second index: b2b3b4b5
        assert 0 <= x < 64
        i, j = ((x // 32) * 2 + (x % 2), (x % 32) // 2)
        # and access to S4, return integer value in [0, 16).
        return S4[i][j]

# 2.3 get_s5 : integer |-> integer
def get_s5(x: int):
        # read x(6-bit integer) and find correspond index in S4 box
        # first index: b1b6 (b6 is MSB of x)
        # second index: b2b3b4b5
        assert 0 <= x < 64
        i, j = ((x // 32) * 2 + (x % 2), (x % 32) // 2)
        # and access to S4, return integer value in [0, 16).
        return S5[i][j]

#  2.4 count_one : string |-> integer
def sum_digit(b: str):
        # read input string
        # and return a number of occurence of '1' in b
        return sum([int(i) for i in b])
# ----------


# ----------
# 3. Main functions

XDT = [[0] * 16 for i in range(64)]
LDT = [[0] * 16 for i in range(64)]

# 3.1 XDT construction
for x in range(64):
    for x_ in range(64):
        d = x ^ x_
        XDT[d][get_s4(x) ^ get_s4(x_)] += 1

# 3.2 LDT construction
for a in range(1, 64):
    for b in range(1, 16):
        for x in range(64):
            LDT[a][b] += (sum_digit(i2b(x & a, 6)) + sum_digit(i2b(get_s5(x) & b, 4))) % 2

for i in range(64):
    for j in range(16):
        LDT[i][j] = 32 - LDT[i][j]

# 3.3 Functions for pretty printing
def print_tablerow(x: list, idx):
    if type(idx) == int: print("| %3X |" % idx, end="");
    else: print("| %3s |" % idx, end="");
    for i in x:
        print("%4s" % i, end="");
    print("|")
    return

def print_tableline(col: int):
    print("+-----+", end="");
    print("----"*col, end="");
    print("+");
    return


# 3.4 outputs
print("CS448 Homework #5");
print("20130143 Yihan Kim");

# 3.4.1 print XDT of S4 box
print("XDT of DES S4-box");
print_tableline(16);
print("|Input|" + " " * 27 + "Output XOR" + " " * 27 + "|");
print_tablerow(range(16), "XOR");

print_tableline(16);
for i in range(64):
    print_tablerow(XDT[i], i);
print_tableline(16);
print();


# 3.4.2 print LDT of S5 box
print("LDT of DES S5-box");
print_tableline(15);
print("|     |" + " " * 29 + "b" + " " * 30 + "|");
print_tablerow(range(1, 16), "a");
print_tableline(15);
for i in range(1, 64):
    print_tablerow(LDT[i][1:], i)
print_tableline(15);
print();
