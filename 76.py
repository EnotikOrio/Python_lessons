#481
arr1 = input().split(", ")
arr2 = sorted(arr1, reverse=True)
res = ""
for i in range(len(arr2)):
    res += arr2[i]
    if i != len(arr2) - 1:
        res += " "
print(res)