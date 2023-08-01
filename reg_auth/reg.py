def add_user(login, password):
    with open("users.txt", "a") as file:
        file.write(f"{login}, {password} \n")

def main():
    while True:
          login = (input("Введіть Логін, або натиснить enter щоб вийти: "))
          if not login:
               break
          password = input("Введіть пароль:")
          add_user(login, password)
if  __name__ == main():
     main()
