def add_user(login, password):
    flag = False
    with open("users.txt", "r") as check:
         for line in check:
            e_login, e_pass = line.strip().split(",")
            if e_login == login:
                flag = True
    if flag:
        print("Користувач з таким логіном існує: ")
        return False
    else:
        print("Ви зареєструвались: ")
        
    with open("users.txt", "a") as file:
        file.write(f"{login}, {password} \n")

def main():
    while True:
          login = (input("Введіть Логін, або натиснить enter щоб вийти: "))
          if not login:
               break
          password = input("Введіть пароль:")
          add_user(login, password)
if  __name__ == "__main__":
     main()
