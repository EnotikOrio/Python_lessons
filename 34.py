x = int(input("Введіть розмір квадрата: "))
for i in range(0, x):
    for j in range(0, x):
        if i == j:
            print('0', end=' ')
        else:
            print("X", end=' ')
    print()
