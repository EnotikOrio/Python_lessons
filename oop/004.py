import random

class Marker:
    def __init__(self, name, height, width, mass, color):
        self.name = name
        self.height = height
        self.width = width
        self.mass = mass
        self.color = color
        pass

def add_marker():
    name = firm[random.randint(0, len(firm) - 1)]
    color = colors[random.randint(0, len(colors) - 1)]
    widht = random.uniform(1.0, 5.0)
    height = random.uniform(5.0, 25.0)
    mass = random.uniform(10.0, 45.0)
    marker = Marker(name,height, widht, mass, color)
    return marker

firm = ["Sharpie", 
        "Copic", 
        "Posca", 
        "Prismacolor", 
        "Sakura", 
        "Faber-Castell", 
        "Uni-ball",
        "Molotow", 
        "BIC", 
        "Zebra Pen"]

colors = ["Red", 
          "Blue", 
          "Green", 
          "Yellow", 
          "Orange", 
          "Purple", 
          "Pink", 
          "Black", 
          "White", 
          "Gray"]

markers = []

t1 = 0

while t1 < 100:
    markers.append(add_marker())
    t1 += 1

for i in range(0, len(markers)):
    print("Назва:",markers[i].name, 
          
          "\nКолір:", markers[i].color, 
          
          "\nШирина:", f"{markers[i].width:.2f}","sm", 
          
          "\nВисота:", f"{markers[i].width:.2f}", "sm", 
          
          "\nМаса:", f"{markers[i].mass:.2f}", "g")
    print("----------------")