import math
def nat(g):
    t1 = 0
    for i in range(2, int(math.sqrt(g))):
        if g % i == 0:
            t1 += 1
        if t1 > 0:
            return "Не просте"
    return "Просте"
print(nat(int(input(""))))
