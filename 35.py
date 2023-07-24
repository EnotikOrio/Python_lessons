import random

t = 0
x = int(input("Введіть розмір квадрата: "))
for i in range(0, x):
    for j in range(0, x):
        r = random.randint(1, 25)
        print(r, end=('\t'))
        if i == j:
            t += r
            
    print()
print()
print(t)
