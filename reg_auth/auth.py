def check(login, password):
    with open("users.txt", "r") as file:
        for line in file:
            e_login, e_pass = line.strip().split(",")
            if e_login == login and e_pass == password:
                return True
        return False
def main():
    while True:
        login = (input("Введіть Логін та пароль що зареєструватися, або натиснить enter щоб вийти: "))
        if not login:
            break
        password = " " + input("Введіть пароль:")
        if check(login, password):
            print("Вхід виканоно: ")
        else:
            print("Невірний логін або пароль:")
if  __name__ == "__main__":
     main()