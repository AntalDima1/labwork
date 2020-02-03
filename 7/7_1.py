n = int(input("n: "))
m = int(input("m: "))

a = [
    [int(input("{0},{1}: ".format(i, j))) for j in range(m)] for i in range(n)
]

S = 0

for i in range(0, n, 2):
    for j in range(0, m, 2):
        el = a[i][j]

        if el < 0:
            S += el

print(S)
