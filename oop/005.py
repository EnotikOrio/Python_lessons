#810

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

length = float(input("Введіть довжину: "))
width = float(input("Введіть ширину: "))

rectangle = Rectangle(length, width)

ar = rectangle.calculate_area()
print("Площа прямокутника:", ar)

