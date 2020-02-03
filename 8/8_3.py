def fib(i):
    if i == 1 or i == 2:
        return 1
    return fib(i-1) + fib(i-2)

s = fib(3) + fib(8)

print(s)