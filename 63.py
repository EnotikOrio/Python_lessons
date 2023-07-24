#ar1 = list(map(int, input().split()))
ar1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ar2 = []
ar3 = []
for i in range(len(ar1)//2-1, -1, -1):
    ar2.append(ar1[i])
    ar3.append(ar1[i+len(ar1)//2])
ar2.extend(ar3)


print(ar1)
print(ar2)
print(ar3) 