#522
x = input("Введіть рядок: ")

arr1 = {}
for c in x:
    if c in arr1:
        arr1[c] += 1
    else:
        arr1[c] = 1
for c in arr1:
    f = arr1[c]
    print(c, f)
