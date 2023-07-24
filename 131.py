from math import sqrt
def g(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
h, v, y, j = map(int, input(" ").split())
print(g(h, v, y, j))