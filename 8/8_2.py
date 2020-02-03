def get_vector(name, dim):
    return [float(input("{0}({1}): ".format(name, i+1))) for i in range(dim)]

def scalar_product(v1,v2):
    products = list(map(lambda c1, c2: c1 * c2, v1, v2))

    s = 0

    for el in products:
        s += el
    
    return s

n = int(input("n: "))

a = get_vector("a", n)
b = get_vector("b", n)
c = get_vector("c", n)

s = 2 * scalar_product(a,b) - 3 * scalar_product(a,c)

print(s)
