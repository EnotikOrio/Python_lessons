symb = '0123456789ABCDEF'
def from_hex(o1):
    res = 0
    t1 = 0
    o1 = str(o1)
    o1 = o1[::-1]
    for i in o1:
        res = res + int(symb.index(i)) * (16 ** t1)
        t1 += 1
    return res
def to_hex(g1):
    res = ""
    while g1 > 0:
        tx = g1 % 16
        res += symb[tx]
        g1 = g1 // 16
    res = res[::-1]
    return res
def to_dec(h1, m1):
    l = len(str(h1))
    res = 0
    for i in range(l):
        tx = h1 % 10 
        res = res + tx * (m1 ** i)
        h1 = h1 // 10
    return res 
def x(x1, j1, y1):
    x1 = to_dec(x1, j1)
    if y1 != 16:
        res = ""
        while x1 > 0:
            res += str(x1 % y1)
            x1 = x1 // y1
        res = res[::-1]
        return res
    else:
        return to_hex(x1)
g, j, y = map(int, input("").split())
print(x(g, j, y))
print(from_hex('FD'))
