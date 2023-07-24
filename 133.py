def year(k):
    if k % 4 == 0:
        if k % 100 == 0 and k % 400 != 0:
            return False
        else:
            return True
    return False
print(year(int(input("введіть рік: "))))