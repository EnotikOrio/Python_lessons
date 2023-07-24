#311
arr1 = input("Введіть рядок: ")
arr2 = input("Введіть набір символів: ")

s = True
i = 0
while i < len(arr2) and s:
    if arr1[i] != arr2[i]:
        s = False
    i += 1
print(s)