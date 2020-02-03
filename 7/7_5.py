n = int(input("n: "))
m = int(input("m: "))

A = [
    [int(input("A[{0},{1}] = ".format(i, j))) for j in range(m)] for i in range(n)
]

count = 0

for r in range(n):
    zero = False
    for c in range(m):
        if A[r][c] == 0:
            zero = True
            break
    if not zero:
        count += 1

print(count)
