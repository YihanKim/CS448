# CS448 Homework #6
# 20130143 Yihan Kim


# function 1.
# fast_expt : (x, k, N) -> (x ^ k) mod N

def fast_expt(x:int, k:int, N:int):
    if k == 0:
        return 1 # x ^ 0 = 1
    elif k == 1:
        return x % N # sometimes x can be greater than N
    else:
        y = fast_expt(x, k // 2, N)
        return y * y * fast_expt(x, k % 2, N) % N


# function 2.
# extended_mod : (b, N) -> a s.t. (bx + ay mod N == 1) for some x, y
def extended_mod(b: int, n: int):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    # b : gcd(b, N)
    # x0, y0 s.t. a * x + b * y = g
    return  (b, x0, y0)


# Problem 2

p2 = 2357
q2 = 2551
M2 = 1234
print("\nProblem 2. given : p = %s, q = %s, M = %s" % (p2, q2, M2))

print("\n1. Key Generation")
n2 = p2 * q2
phi_n2 = (p2 - 1) * (q2 - 1)

# 13 and phi_n2 are coprime
e2 = 13
d2 = extended_mod(e2, phi_n2)[1] % phi_n2
print("n = %s, e = %s, d = %s" % (n2, e2, d2))

print("\n2. Encryption")
print("Calculating M ** e mod n = %s ** %s mod %s ..." % (M2, e2, n2))
C2 = fast_expt(M2, e2, n2)
print("encrypted message of M = %s : C = %s" % (M2, C2))


print("\n3. Decryption")
print("Calculating C ** d mod n = %s ** %s mod %s ..." % (C2, d2, n2))
M2_ = fast_expt(C2, d2, n2)
print("Decrypted message of C = %s : M' = %s" % (C2, M2_))
print("Compare : %s = %s" % (M2, M2_))

# Problem 3
p3 = 885320963
q3 = 238855417
M3 = 1234567
print("\nProblem 3. given : p = %s, q = %s, M = %s" % (p3, q3, M3))
print("\n4. Key Generation")
n3 = p3 * q3
phi_n3 = (p3 - 1) * (q3 - 1)

# 103 and phi_n3 are coprime
e3 = 103
d3 = extended_mod(e3, phi_n3)[1] % phi_n3
print("n = %s, e = %s, d = %s" % (n3, e3, d3))
#print("validity : %s" % ((e3 * d3) % phi_n3))

print("\n5. Encryption")
print("Calculating M ** e mod n = %s ** %s mod %s ..." % (M3, e3, n3))
C3 = fast_expt(M3, e3, n3)
print("encrypted message of M = %s : C = %s" % (M3, C3))

print("\n6. Decryption")
print("Calculating C ** d nod n = %s ** %s mod %s ..." % (C3, d3, n3))
M3_ = fast_expt(C3, d3, n3)
print("Decrypted message of C = %s : M' = %s" % (C3, M3_))
print("Compare : %s = %s" % (M3, M3_))
