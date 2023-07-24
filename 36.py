n = 4
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print('X', end='  ')
        else:
            print('0', end='  ')
    print()
