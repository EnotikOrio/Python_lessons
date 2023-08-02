def delete_user():
    username = input("Введите логин пользователя, которого хотите удалить: ")
    with open("users.txt", "r") as file:
        lines = file.readlines()
    deleted = False
    with open("users.txt", "w") as file:
        for line in lines:
            login, password = line.strip().split(', ')
            if login != username:
                file.write(f"{login}, {password}\n")
            else:
                deleted = True
    if deleted:
        print(f"Пользователь с логином '{username}' успешно удален.")
    else:
        print(f"Пользователь с логином '{username}' не найден.")
