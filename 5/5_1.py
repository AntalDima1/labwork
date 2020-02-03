n = int(input("n: "))
a = float(input("a: "))

P = 1

for i in range(n):
    P *= a + i

print(P)