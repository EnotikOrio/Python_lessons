import random
x = []
v = random.randint(1, 100)

for i in range(0, v):
    c = random.randint(1, 1000)  
    x.append(c)
t = len(x)
print(t)
print(v)
print(x)
a = int(input("Введіть число кількість повторень якого ви хочете дізнатися: "))
t2 = 0
for j in range(0, v):
    if x [j] == a:
        t2 += 1
print(t2)

t3 = x.count(a)
print(t3)

x.pop(0)
print(x)

x.reverse()
print(x)

s1 = sum(x)
print(s1)

mx = max(x)
print(mx)

mi = min(x)
print(mi)

x.sort(reverse=True)
print(x)

serch = x.index(a)
print(serch)

x.remove(a)
print(x)

x.insert(1, 0)
print(x)

x.clear()
print(x)