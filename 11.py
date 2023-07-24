number = input("Введіть тризначне число: ")

if len(number) != 3 or not number.isdigit():
    print("Некоректне введення!")
else:
    x = int(number[0])
    c = int(number[1])
    v = int(number[2])
    
    if x > v:
        result = int(number) * 3
        print("Результат:", result)
    elif x < v:
        result = int(str(v) + str(c) + str(x))
        print("Результат:", result)
    else:
        result = int(number) * c
        print("Результат:", result)
