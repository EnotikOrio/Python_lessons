def delete_user():
    users = input("Введіть логін користувача котрий хочете видалити: ")
    with open("users.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open("users.txt", "w", encoding="utf-8") as file:
        delete = False
        for i, line in enumerate(lines):
            if line.strip() == f"{users}":
                delete = True
            else:
                file.write(line)
        if delete:
            print("Користувача видалено: ")
        else:
            print("Користувача не знайдено: ")
    print(f"{users}")
    print(line.strip() == f"{users}")
delete_user()