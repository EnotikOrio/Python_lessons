#465
arr1 = list(map(int, input().split()))
x = int(input("Введіть індекс котрий хочете видалити: "))

if x < len(arr1):
    arr1.pop(x)
print(arr1)