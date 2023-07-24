#461
arr1 = input()
arr2 = arr1.split('_')

case = ""
for i in arr2:
    case += i[0].capitalize() + i[1:]
print(case)