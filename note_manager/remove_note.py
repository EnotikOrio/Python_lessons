import os

def remove_note():
    note_title = input("Введіть назву нотатки котру хочете видалити: ")
    with open("notes.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()
    deleted = False
    with open("notes.txt", "w", encoding='utf-8') as file:
        for line in lines:
            title, content = line.strip().split(', ')
            print(title)
            print(content)
            if title != "Заголовок: " + note_title:
                file.write(f"{title}, {content}\n")
            else:
                deleted = True
    if deleted:
        print(f"Нотатка '{note_title}' вдало видалена.")
    else:
        print(f"Нотатка '{note_title}' не знайдена.")
remove_note()