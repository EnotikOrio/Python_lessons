import math

class Circle:
    def __init__(self, r):
        self.r = r
    def ress(self):
        return self.r * math.pi ** 2
    
c1 = Circle(int(input("перше коло: ")))

c2 = Circle(int(input("друге коло: ")))

print(c1.ress())
print()
print(c2.ress())

