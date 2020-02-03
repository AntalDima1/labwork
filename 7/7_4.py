n = int(input("n: "))

matrix = [
    [int(input("{0},{1}: ".format(i, j))) for j in range(n)] for i in range(n)
]

for i in range(0, n, 2):
    matrix[i].sort()

for row in matrix:
    print(row)
