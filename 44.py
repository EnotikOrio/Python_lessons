#дана таблиця n х m. знайти сумму кожного стопчика та вказати в якому стопчику найбільша сумма знайти найбільше число в таблиці. кожне число - випадкове в проміжку від 10 до 99
import random

n = int(input("n = "))
m = int(input("m = "))
s_max = 0
res_n = 0
mx = 0


for i in range(1, n + 1):
    s = 0
    for j in range(1, m + 1):
        x = random.randint(10, 99)
        s += x
        if mx < x:
            mx = x
        print(x, end='  ')
    print(' |', s, end='\t')
    if s > s_max:
        s_max = s
        res_n = i

    print()

print()
print("Найбільше число в таблиці:", mx)
print("Найбільша сума рядка:", s_max)
print("Рядок з найбільшою сумою:", res_n)

#Знайти найбільше число в таблиці. знайти сумму всіх рядків та той рядок в якому сумма найбільша