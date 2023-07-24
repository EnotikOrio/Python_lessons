x = int(input("Введіть кількість рядків: "))
y = int(input("Введіть кількість стопців: "))
t = 1
for i in range(0, x):
    for j in range(0, y):
        print(t * t, end='\t')
        t += 1
    print()
