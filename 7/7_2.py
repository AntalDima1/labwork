import math

def el(i,j):
    if (i*j) % 2 == 0:
        return math.factorial(j)
    else:
        s = 0
        for x in range(1, i+1):
            s += x
        return s

n = int(input("n: "))
m = int(input("m: "))

A = [
    [el(i,j) for j in range(1,m+1)] for i in range(1,n+1) 
]

A1 = []

for row in A:
    A1 += row

print(A1)