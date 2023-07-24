#466
arr1 = list(map(int, input().split()))
k, c = map(int, input("Введіть два цілих числа: ").split())

arr1.append(None)

for i in range(len(arr1) - 2, k - 1, -1):
    arr1[i + 1] = arr1[i]

arr1[k] = c
for i in range(len(arr1)):
    if i == len(arr1) - 1:
        print(arr1[i], end=" ")
    else:
        print(arr1[i], end=" ")


