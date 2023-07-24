#660(знайти всі дільники числа)

def is_per_num(num):
    div = 0

    for i in range(1, num):
        if num % i == 0:
            div += i

    return div == num

i = input().split()
for j in i:
    num = int(j)
    res = is_per_num(num)
    print(res)
