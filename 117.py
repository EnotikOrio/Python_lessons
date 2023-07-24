#613
def f(a, b, c):
    return max(a, b, c)

i1 = input().split()
i2 = input().split()
i3 = input().split()

res1 = f(int(i1[0]), int(i1[1]), int(i1[2]))
res2 = f(int(i2[0]), int(i2[1]), int(i2[2]))
res3 = f(int(i3[0]), int(i3[1]), int(i3[2]))

print(res1)
print(res2)
print(res3)
