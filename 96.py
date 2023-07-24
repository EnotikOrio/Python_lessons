#508

arr1 = {
    232: "Alice",
    550: "Bob",
    190: "Jack"
}

arr2 = "Hi, to all!"

arr3 = []

while True:
    user_id = input("Введіть ідентифікатор користувача (або ентер для завершення): ")
    if not user_id:
        user_ids = list(map(int, arr3))
        break
    arr3.append(user_id)

for user_id in user_ids:
    print("Hi,", arr1.get(int(user_id), arr2) + "!")


