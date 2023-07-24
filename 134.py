def s(m, f):
    res = 1
    t1 = ""
    for i in range(f):
        res = res * m
        t1 = t1 + str(m) + " * "
    return str(m) + " ** " + str(f) + " ----> " + t1[0:len(t1)- 2:] + " = " + str(res)
g, y = map(int, input(" ").split())
print(s(g, y))
