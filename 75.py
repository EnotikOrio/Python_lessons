#469
arr1 = list(map(int, input().split()))
arr2 = list(reversed(arr1))
res = 0
for i in arr2:
    res = res * 10 + i
print(res)