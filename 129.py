#628

def even(s):
    n = s.split()
    res = []
    for num in n:
        if int(num) % 2 == 0:
            res.append(int(num))
    return res

i = input()
print(even(i))
