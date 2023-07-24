#412
n = int(input("n="))
arr1 = []
arr1 = list(map(int, input().split()))

for i in range(0, len(arr1)):
    if arr1[i] < n:
        print(arr1[i], end=" ")