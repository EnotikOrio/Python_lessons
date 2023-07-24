#411

'''n = list(map(int, input().split()))
for i in range(0, len(n)):
    if i % 2 == 0:
        print(n[i], end=" ")

n2 = n[0: :2]
print(n2)'''

print(list(map(int, input().split()))[0::2])




