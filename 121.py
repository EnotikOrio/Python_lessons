def wrap(n, a):
    begin = f"<{n}>"
    end = f'</{n}>'
    return begin + a + end
x, y = map(str, input("").split())
print(wrap(x, y))
