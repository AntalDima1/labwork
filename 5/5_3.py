import math

epsilon = float(input("epsilon: "))
x = float(input("x: "))

S = 2
n = 1

adder = epsilon+1

while adder > epsilon:
    adder = (((x-1)/(x+1)) ** (2*n-1)) / (2*n - 1)
    S += adder
    n += 1

print(math.log(x))
print(S)
