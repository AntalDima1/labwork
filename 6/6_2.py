x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

n = int(input("n: "))

A = [x,x,y]

for i in range(4,n+1):
    A.append(
        A[i-3] + (A[i-2])/(2**(i-2)) * A[i-4]
    )

larger_z = list(filter(lambda el: el > z, A))

print(A)
print("larger than z:", len(larger_z))