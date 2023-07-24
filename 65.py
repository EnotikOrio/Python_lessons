'''n1 = list(map(int, input().split()))
s1 = n1[len(n1) // 2:]
res = sum(s1)
print(s1)
print(res)


n2 = list(map(int, input().split()))
n2 = n2[-2:] + n2[:-2]
res2 = sum(n2)
print(n2)
print(res2)'''

l1 = input().split()
s2 = sorted(l1)
print(s2)


l2 = input().split()
r1 = sorted(l2, reverse=True)
print(r1)

n3 = list(map(int, input().split()))
r2 = n3[::-1]
print(r2)
