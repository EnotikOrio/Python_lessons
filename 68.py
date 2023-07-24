arr1 = list(map(int, input().split()))
arr2 = []

cort1 = set(arr1)

for i in cort1:
    if arr1.count(i) % 2 == 0:
        arr2.append(i)
print(arr2)

for i in arr1:
    for j in arr2:
        if i == j:
            print(i, end=" ")
    