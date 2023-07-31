#В файлі а.txt є 3 числа записаних через пробіл 
#Знайти їх сумму та добудок та записати в файл res.txt 
import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

f1 = open('a.txt', 'w')
f1.write(f"{num1} {num2} {num3}")
f1.close()

f1 = open('a.txt', 'r')
num = list(map(int, f1.readline().split()))
f1.close()

s = sum(num)
p = 1
for n in num:
    p *= n

res = open('res.txt', 'w')
res.write(f"Сума: {s}\n")
res.write(f"Добуток: {p}\n")
res.close()
