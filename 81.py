#306
arr1 = input("Введіть рядок (довжина не менше 2): ")
if len(arr1) >= 2:
    l = arr1[-2:]
    res = l * 5
    print(res)
else:
    print("Довжина рядка повинна бути не менше 2.")