import random
Win = 5
user_bal = 0
pc_bal = 0

while user_bal < Win and pc_bal < Win:
    print("Оберіть: 1 - камень, 2 - Ножиці, 3 - Папір")
    user_choice = int(input("Оберіть варіант: "))

    if user_choice < 1 or user_choice > 3:
        print("ви обрали не коректний варіант")
        continue

    pc_choice = random.randint(1, 3)
    print("Ви обрали:", user_choice)
    print("Пк обрал:", pc_choice)

    if (
        (user_choice == 1 and pc_choice == 2) or
        (user_choice == 2 and pc_choice == 3) or
        (user_choice == 3 and pc_choice == 1)
    ):
        print("Ви виграли")
        user_bal += 1
    elif user_choice == pc_choice:
        print("Ничья")
    else:
        print("Ви програли")
        pc_bal += 1

    print("Поточний рахунок: Гравець", user_bal, "-Пк", pc_bal)
    print()

if user_bal == Win:
    print("Ви виграли у грі")
elif pc_bal == Win:
    print("Ви програли у грі")
