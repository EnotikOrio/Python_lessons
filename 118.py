#614
def f(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

i1 = input().split()
i2 = input().split()

res1 = f(int(i1[0]), int(i1[1]), int(i1[2]))
res2 = f(int(i2[0]), int(i2[1]), int(i2[2]))

print(res1)
print(res2)
