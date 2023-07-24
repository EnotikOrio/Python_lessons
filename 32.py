x = int(input("Введіть кількість рядків: "))
y = int(input("Введіть кількість стопців: "))
t = x * y
for i in range(0, x):
    for j in range(0, y):
        print(t, end='\t')
        t -= 1
    print()
