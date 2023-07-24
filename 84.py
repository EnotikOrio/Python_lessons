x1 = int(input("x1 = "))
x2 = int(input("x2 = "))
arr1 = []
arr2 = []
t1 = 0
s1 = 0
while x1 > 0:
    arr1.append(x1 % 10)
    x1 = x1 // 10
    t1 += 1
arr1.reverse()
print(arr1)

while x2 > 0:
    arr2.append(x2 % 10)
    x2 = x2 // 10
    t1 += 1
arr2.reverse()
arr3 = arr1 + arr2
print(arr3)

for i in range(0, len(arr3)):
    s1 += arr3[i] * (10 ** (t1 - 1 - i))
    print(arr3[i] * (10 ** (t1 - 1 - i)))
print(s1)
print(s1 ** 2)