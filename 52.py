s = 0

while s < 100:
    n = int(input("Введіть число: "))
    s += n
    if s <= 100:
        break
print("Сума цифр перевищила 100")