import random


t1 = 0
t2 = 0
x = -7

for i in range(0, 10):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    c = a * b
    r = int(input(str(a) + " * " + str(b) + " = "))
    if r == c:
        print("Правильно")
        t1 += 1
    else:
        t2 += 1
        print("Неправильно")
print("Правельных ответов: ", t1)
print("Неправельных ответов: ", t2)
k1 = t1 / 10 * 100
k2 = t2 / 10 * 100
print("Процент правильных ответов:", k1)
print("Процент неправельных ответов:", k2)

if k1 >= 0 and k1 < 25:
    print("Ваш уровень начальный")
elif k1 >= 25 and k1 < 50:
    print("Ваш уровень выше начального")
elif k1 >= 50 and k1 < 75:
    print("Ваш уровень средний")
elif k1 >= 75 and k1 <= 100:
    print("Ваш уровень высокий")
else:
    print("Ошибка")
 