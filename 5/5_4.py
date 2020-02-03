x_0 = 1
x_i = 0

for i in range(1, 11):
    x_i = x_0 + 2*i
    x_0 = x_i

print(x_i) 