#462
arr = (input().split())
n1 = arr.count('A')
n2 = len(arr)
res = n1 / n2 
res = float("{:.2f}".format(res))
print(res)