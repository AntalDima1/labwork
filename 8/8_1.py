import math


def f(x, y):
    if x > y:
        return x ** 3 + math.sqrt(x ** 2 + y ** 4)
    else:
        return (x ** 2 - 2 * x + math.sqrt(x))/(x ** (3/5))


a = float(input("a: "))
b = float(input("b: "))

print(f(a, b) + f(2, a) + 2)
