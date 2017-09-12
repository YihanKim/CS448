
# CS448 Assignment #2

# 20130143 Yihan Kim
# Python 3.4

# 0. Purpose
# verify the design criteria for S4_box in DES(Data Encryption Standard)
# -- especially S4(x) ^ S4(x ^ 12) differs at least 2 bits

# 1. Constant

# 1.1 S4_box : listof(listof(int))

# describing S4_box information
# each number is accessible by using S4[i][j],
# where 0 <= i < 4 and 0 <= j < 16.

S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]];


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


#  2.3 count_one : string |-> integer

def sum_digit(b: str):
        # read input string
        # and return a count of occurence of '1' in b
        return sum([int(i) for i in b])


# 3. Main routine
# 3.1 Calculation, formatting and printing

# 3.1.1 table column design
# int x : iterating number
# int x^12 : (implies x XOR 001100)
# int S4(x), S4(x^12) : result of S4 function call
# binary diff : S4(x) XOR S4(x ^ 12)
# int count : # of 1 in diff, nonnegative integer less or eq to 4
# bool >2 : count is greater or equal to 2?
# table_head contains string that informs meaning of each column

table_column = 7
table_head = ("%8s %8s %8s %8s %8s %8s %8s" %
        ('x', 'x^12', 'S4(x)', 'S4(x^12)', 'diff', 'count', '>2'))
print(table_head)


# 3.1.2 split line (for pretty view)
split_line = '-' * (8 * table_column + 1 * (table_column - 1))
print(split_line)


#3.1.3 table contents
# for each x in [0, 64), calculate and save values
# of each column with string type into list table_items.

table_items = list()
for i in range(64):
        diff =i2b(get_s4(i) ^ get_s4(i ^ 12), 4)
        table_row = ("%8s %8s %8s %8s %8s %8s %8s" % (
                i2b(i, 6),                      # x
                i2b(i ^ 12, 6),                 # x ^ 12
                i2b(get_s4(i), 4),              # S4(x)
                i2b(get_s4(i ^ 12), 4),         # S4(x ^ 12)
                diff,                           # S4(x) ^ S4(x ^ 12)
                sum_digit(diff),                # #1(S4(x) ^ S4(x ^ 12))
                sum_digit(diff) >= 2            # #1(S4(x) ^ S4(x ^ 12)) >= 2
                )
        )
        table_items.append(table_row)
        print(table_row)

# 3.2 File I/O
# write down the entire result into the output.txt

with open("output.txt", "w") as f:
        f.write(table_head + "\n")
        f.write(split_line + "\n")
        for table_row in table_items:
                f.write(table_row + "\n")

# end of code
