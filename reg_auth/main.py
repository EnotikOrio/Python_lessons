import auth
import reg
import remove

a = int(input("Введіть дію, яку хочете зробити: 1. Увійти, 2. Зареєструватися, 3. Видалити Користувача: "))

if a == 1:
    auth.main()
elif a == 2:
    reg.main()
elif a == 3:
    remove.delete_user()
else:
    print("Такого варіанту немає")
