import random
r = random.randint(30, 50)
x = []
t1 = 0
t2 = 0
while t1 != r:
    t1 += 1
    v = random.randint(10, 1000)
    x.append(v)
print(x)

g = x[0] + x[-1]
print("Сумма першого та останньго:",g)

t2 = x[0]
x[0] = x[-1]
x[-1] = t2

print(x)
s1 = 0
for i in range(0, 15):
    s1 += x[i]
print(s1)

s2 = 0

for j in range(-1, -16, -1):
    s2 += x[j]
print(s2)

l = s1 + s2
print(l)

s3 = 0
s4 = 0
for k in range(0, r):
    if x[k] % 2 == 0:
        s3 += 1
        x[k] = x[k] / 2
    elif x[k] % 2 == 1:
        s4 += 1
print("Цілих значень:",s3 ,"Не цілих значень:", s4)