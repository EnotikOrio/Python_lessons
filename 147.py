#Рекрсією вивести значення від А до Б
def p(A, B):
    if A <= B:
        print(A)
        p(A + 1, B)

A = int(input())
B = int(input())

p(A, B)
