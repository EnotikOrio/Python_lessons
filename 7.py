a = int(input("Введите значение: "))
b = int(input("Введите значение: "))
x = input("Введите знак: +, -, *, /, **: ")
if x == "+":
    print(a + b)
elif x == "-":
    print(a - b)
elif x == "*":
    print(a * b)
elif x == "/":
    if b == 0:
        print("нельзя на ноль делить")
    else:
        print(a / b)
elif x == "**":
    print(a ** b)
else: 
    print("Разрабы такого не добовляли")
print("Все сделано")