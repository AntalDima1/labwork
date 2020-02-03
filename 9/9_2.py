class Autopart:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    
    def __str__(self):
        return "{0} ({1}, made in {2})".format(self.name, self.model, self.year)

n = int(input("n: "))

autoparts = []

for i in range(n):
    name = input("Autopart #{0} Name: ".format(i+1))
    model = input("Autopart #{0} Model: ".format(i+1))
    year = int(input("Autopart #{0} Year: ".format(i+1)))

    autoparts.append(Autopart(name, model, year))

q = input("Search: ")

results = list(filter(lambda a: q in str(a), autoparts))

for a in results:
    print(a)
