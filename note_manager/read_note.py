import os
import add_note

def read_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.read()
            print(notes)
    else:
        print("На данний момент жодноє нотатки немає. Створіть першу нотатку: ")
        add_note.create_note()