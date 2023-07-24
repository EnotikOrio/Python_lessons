#662

def g(s2):
    g = {'A': [], 'B': [], 'C': [], 'D': [], 'F': []}

    for s1 in s2:
        if 90 <= s1 <= 100:
            g['A'].append(s1)
        elif 80 <= s1 <= 89:
            g['B'].append(s1)
        elif 70 <= s1 <= 79:
            g['C'].append(s1)
        elif 60 <= s1 <= 69:
            g['D'].append(s1)
        else:
            g['F'].append(s1)
    return g

i = input().split()
s1 = [int(s2) for s2 in i]

res = g(s1)
print(res)
