import os

def create_note():
    title = input("Введіть заголовок замітки: ")
    content = input("Введіть текст замітки: ")
    with open("notes.txt", "a", encoding='utf-8') as file:
        file.write(f"\nЗаголовок: {title}\n{content}")
