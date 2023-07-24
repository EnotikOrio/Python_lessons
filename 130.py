#636

def c(s):
    num = s.split()
    return [int(num) for num in num]

def d(num):
    return list(set(num))

i = input()
n = c(i)
res = d(n)
print(res)
