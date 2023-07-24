x1 = input("x1 = ")
x2 = input("x2 = ")
x1r = x1[::-1]
x2r = x2[::-1]
res1 = int(x1) * int(x1r)
res2 = int(x2) * int(x2r)
res3 = str(res1) + str(res2)
print(res1)
print(res2)
print(res3)