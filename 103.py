#521
arr1 = {
    'Alex': 85,
    'Barbara': 92,
    'Charlie': 78,
    'David': 88,
    'Emily': 76
}

arr2 = sum(arr1.values()) / len(arr1)

arr3 = []
for i in arr1:
    if arr1[i] > arr2:
        arr3.append(i)

for j in arr3:
    print(j)
