#509

arr1 = {
    "key": 3,
    "mace": 1,
    "gold coin": 24,
    "lantern": 1,
    "stone": 10
}

print("Предметы:")
t = 0
for item, q in arr1.items():
    print(q, item)
    t += q

print("Число предметів:", t)
