#658  

def pre_stats(pre):
    mo = ['January', 
              'February', 
              'March', 
              'April', 
              'May', 
              'June', 
              'July', 
              'August', 
              'September', 
              'October', 
              'November', 
              'December']

    t1 = sum(pre)
    a1 = t1 / len(pre)
    max_p = max(pre)
    min_p = min(pre)
    max_m = mo[pre.index(max_p)]
    min_m = mo[pre.index(min_p)]

    return t1, a1, (max_p, max_m), (min_p, min_m)

i1 = input().split()
pre = []
for val in i1:
    pre.append(int(val))

res = pre_stats(pre)
print(res)
