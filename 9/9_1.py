class Worker:
    def __init__(self, passport, education, spec, post, salary):
        self.passport = passport
        self.education = education
        self.spec = spec
        self.post = post
        self.salary = salary
    
    def __str__(self):
        return "{0} ({1}, {2}, {3}, {4})".format(self.passport, self.education, self.spec, self.post, self.salary)

class WorkerDB:
    def __init__(self):
        self.db = []

    def add_worker(self, w):
        self.db.append(w)

    def remove_worker(self, w):
        self.db.remove(w)
    
    def write_to_file(self):
        with open("workers.txt", "w") as f:
            for w in self.db:
                f.write(str(w)+"\n")
    
    def search(self, query):
        return list(filter(lambda w: query in str(w), self.db))

db = WorkerDB()

w1 = Worker("Ivan Ivanov", "Full", "Physics", "Engineer", 1000)
w2 = Worker("Petro Petrovich", "Bachelor", "Music", "Sales Manager", 800)
w3 = Worker("Mixail Mixialov", "Master", "Chemistry", "Supervisor", 1100)

db.add_worker(w1)
db.add_worker(w2)
db.add_worker(w3)
db.write_to_file()

query = input("Search: ")

for w in db.search(query):
    print(w)
