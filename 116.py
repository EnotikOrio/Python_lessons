#611

def f():
    s = input("Введіть рядок: ")
    n = int(input("Введіть ціле число n: "))

    if len(s) < n:
        return s
    else:
        return s[:n]
res = f()
print(res)