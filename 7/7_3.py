A = [[float(input("A[{0}, {1}] = ".format(i,j))) for j in range(2)] for i in range(2)]

det = A[0][0] * A[1][1] - A[0][1] * A[1][0]

print(det)