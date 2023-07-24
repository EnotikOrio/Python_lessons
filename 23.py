n = int(input("Скільки значень ви хочете ввести? "))
ns = []
for i in range(n):
    num = int(input("Введіть число: "))
    ns.append(num)

max_n = max(ns)
min_n = min(ns)

print("Найбільше число: ", max_n)
print("Найменше число: ", min_n)
