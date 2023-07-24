s1 = input('s1 = ')
arr1 = {}
for i in s1:
    if i in arr1:
        arr1[i] += 1
    else:
        arr1[i] = 1 
print(arr1)