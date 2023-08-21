#811

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_radius(self):
        return 2 * math.pi * self.radius

radius = float(input("Введіть радіус: "))

circle = Circle(radius)

area = circle.calculate_area()
rad = circle.calculate_radius()

print("Площа круга:", area)
print("Довжина кола:", rad)
