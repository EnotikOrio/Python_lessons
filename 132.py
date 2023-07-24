def bank(n, p, m):
    p1 = n * (1 + p / 100) ** m
    return p1  
h, j, y = map(int, input(" ").split())
print(bank(h, j, y))