import os

def delete_note():
    note_title = input("Введіть заголовок нотатки котру потрібно видалити: ")
    with open("notes.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open("notes.txt", "w", encoding="utf-8") as file:
        delete = False
        for i, line in enumerate(lines):
            if line.strip() == f"Заголовок: {note_title}":
                delete = True
                for i in range(2):
                    i += 1
            else:
                file.write(line)
        if delete:
            print("Нотатку видалено: ")
        else:
            print("Нотатку не знайдено: ")
    print(f"Заголовок: {note_title}")
    print(line.strip() == f"Заголовок: {note_title}")
delete_note()