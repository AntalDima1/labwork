n = int(input("n: "))

A = [float(input("A {0} = ".format(i))) for i in range(n)]

A.sort()

print(A)