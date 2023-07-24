#ar1 = list(map(int, input().split()))
ar1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ar2 = []
ar3 = []
for i in range(0, 8,2):
    ar2.append(ar1[i])
    ar3.append(ar1[i+1])
print(ar1)
print(ar2)
print(ar3) 