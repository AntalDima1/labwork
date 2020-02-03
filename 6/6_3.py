n = int(input("n: "))

x = [float(input("x({0}): ".format(i+1))) for i in range(n)]
y = [float(input("y({0}): ".format(i+1))) for i in range(n)]

z = list(map(lambda x_c, y_c: x_c + y_c, x, y))

print("x + y =", z)