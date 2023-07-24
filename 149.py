#694
def r(num, ind):
    if ind == len(num):
        return 0
    return num[ind] + r(num, ind + 1)

i = map(int, input("").split())
numb = [int(num) for num in i]

res = r(numb, 0)
print(res)

