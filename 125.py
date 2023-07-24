def change_string(s1, s2):
    l1 = len(s1) // 2
    if l1 // 2 != 0:
        return s1[0:l1:] + s2 + s1[l1::]
    else:
        return s1[0:l1:] + s2 + s1[l1 + 1::] 
a, b = map(str, input("").split())
print(change_string(a, b))