#619
def i(l):
    v = "aeiouAEIOU"
    if l in v:
        return True
    else:
        return False

i1 = input()
i2 = input()

res1 = i(i1)
res2 = i(i2)

print(res1)
print(res2)
