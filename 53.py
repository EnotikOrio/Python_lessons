import random
print('Оберіть будьласка рівень: \n 1: 5 спроб; 10 значень \n 2: 10 спроб; 100 значень \n 3: 15 спроб; 1000 значень')
r = int(input("Оберіть рівень: "))
k = 0
if r == 1:
    x1 = random.randint(1, 10) 
    k = 10
    t1 = 5
elif r == 2:
    x1 = random.randint(1, 100)
    k = 100
    t1 = 10
elif r == 3:
    x1 = random.randint(1, 1000)
    k = 1000
    t1 = 15
else:
    print("Не правильно обранний рівень")
if r == 1 or r == 2 or r == 3:
    n = 0
    t2 = 0
    while x1 != n and t1 != 0:
        n = int(input("введіть число від 1 до " + str(k) + ":"))
        t1 -= 1
        t2 += 1
        if n < x1:
            print("більше")
        elif n > x1:
            print("менше")
        elif n == x1:
            print("Ви вгадали")
    if t1 == 0:
        print("Ви викорастовали всі спроби")
    if t1 != 0:
        print('Ви використовали спроб:',t2 )

    