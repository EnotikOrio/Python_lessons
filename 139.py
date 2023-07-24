#661

def calc_in():
    cat = {'A': 0, 'B': 0, 'C': 0}

    for i in range(3):
        x = input()
        p = float(input())
        tick = int(input())
        cat[x] += p * tick

    tot_inc = sum(cat.values())
    return cat, tot_inc

res, tot_inc = calc_in()
print(res, tot_inc)
