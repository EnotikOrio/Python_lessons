#ar1 = list(map(int, input().split()))
ar1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1 = len(ar1)//2
l2 = len(ar1)
ar2 = ar1[l1::-1]
ar3 = ar1[l2:3:-1]

print(ar1)
print(ar2)
print(ar3) 
