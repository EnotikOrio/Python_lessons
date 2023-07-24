import random

A = 1
B = 100

t1 = 0  
t2 = 0  

for i in range(25):
    n = random.randint(A, B)
    print(n)  
    if n % 2 == 0:  
        t1 += n
    else:
        t2 += n

print("Сума парних чисел:", t1)
print("Сума непарних чисел:", t2)
