import auth
import reg

a = int(input("Введіть дію, яку хочете зробити: 1. Увійти, 2. Зареєструватися: "))

if a == 1:
    auth.main()
elif a == 2:
    reg.main()
else:
    print("Такого варіанту немає")
