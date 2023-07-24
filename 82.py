#309
arr1 = input("Введіть рядок: ")
w1 = arr1.split()
res = ''
for w in w1:
    res += w.capitalize() + ' '
res = res.rstrip()
print(res)