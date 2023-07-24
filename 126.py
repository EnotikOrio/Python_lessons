#626 

def h(num):
    histo = ""
    for n in num:
        histo += "*" * int(n) + "\n"
    return histo

i = input().split(",")
res = h(i)
print(res)
