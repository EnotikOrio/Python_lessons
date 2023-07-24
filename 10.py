number = input("Введіть число: ")

last_digit = int(number[-1])

if last_digit == 0:
    print("Нуль")
elif last_digit == 1:
    print("Один")
elif last_digit == 2:
    print("Два")
elif last_digit == 3:
    print("Три")
elif last_digit == 4:
    print("Чотири")
elif last_digit == 5:
    print("П'ять")
elif last_digit == 6:
    print("Шість")
elif last_digit == 7:
    print("Сім")
elif last_digit == 8:
    print("Вісім")
elif last_digit == 9:
    print("Дев'ять")
else:
    print("Некоректне введення!")
