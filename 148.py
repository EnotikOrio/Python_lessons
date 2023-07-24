#697
def r():
    num = int(input())
    if num != 0:
        r()
    print(num)

r()
