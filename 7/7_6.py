n = int(input("n: "))
m = int(input("m: "))

A = [
    [int(input("A[{0},{1}] = ".format(i, j))) for j in range(m)] for i in range(n)
]


existing = set()
targets = []

for row in A:
    for el in row:
        if el in existing:
            targets.append(el)
        else:
            existing.add(el)

max_el = targets[0]

for el in targets:
    if el > max_el:
        max_el = el

print(max_el)