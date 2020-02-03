n = int(input("n: "))

a = [float(input("#{0}: ".format(i))) for i in range(n)]

sum = 0

for el in a:
    sum += el

avg = sum / n

print(avg)