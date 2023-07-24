def in_squer(x, y):
    if x <= 2 and y <= 2 and x >= 0 and y >= 0:
        return 'Yes'
    return "No"
a, b = map(int, input("").split())
print(in_squer(a, b))