import random

s = 0
ro = int(input("Введіть розмір квадрата: "))
for r in range(ro):
    for c in range(ro):
        h = random.randint(1, 25)
        print(h, end=('\t'))
        if r + c == ro - 1:
            s += h
            
    print()
print()
print("Сума значень на побічній діагоналі:", s)
