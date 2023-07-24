#Знайти добуток всіх чисел від А до Б рекурсією
def recu(A, B):
    if A > B:
        return 1
    else:
        return A * recu(A + 1, B)

A = int(input())
B = int(input())

result = recu(A, B)
print(result)
