import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Vector2D({0},{1})".format(self.x, self.y)

    def ask_user(self):
        self.x = float(input("x = "))
        self.y = float(input("y = "))

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        self.x /= self.length()
        self.y /= self.length()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

# TEST
v1 = Vector2D(2,3)
v2 = Vector2D(-3, 2)

print(v1)
print(v1.length())
print(v1+v2)
print(v1-v2)
print(v1*v2)

v2.normalize()
print(v2)