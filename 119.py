#618
def f(s):
    if s.startswith("Is"):
        return s
    else:
        return "Is " + s

i1 = input()
i2 = input()

res1 = f(i1)
res2 = f(i2)

print(res1)
print(res2)
