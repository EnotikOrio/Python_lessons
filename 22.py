import random

a = int(input("Початкове значення: "))
b = int(input("Кінцеве значення: "))
t1 = 0
t2 = 0

for i in range(1, 101):
    x = random.randint(a, b)
    print(x, end=" ")
    if x % 2 == 0:
        t1 += a
    else:
        t2 += 1
print()
print(t1)
print(t2)

if t1 > t2:
    print("Парних більше")
elif t2 > t1:
    print("Непарних більше")
else:
    print("кількість однакова")


 
#Пк генерує 100 випадкових чисел в проміжку від А до В знайти кількість парних та не парних та порівняти їх кількість\
