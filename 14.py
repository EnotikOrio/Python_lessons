t1 = 0
t2 = 0
for x in range(0, 5):
    n = int(input("Введите " + str(x + 1) + " Значення: "))
    if x % 2 == 0:
        t1 += 1
    else:
        t2 += 1
print("Парных: ", t1)
print("Непарных: ", t2)

