import os
import remove_note
import add_note
import read_note

while True:
    print("1 = Щоб створити нотатку, \n2 = Щоб переглянути всі нотатки, \n3 = Щоб видалити нотатку, \n4 = Щоб вийти\n")
    ch = int(input("зробіть свій вибір: "))
    if ch == 1:
        add_note.create_note()
    elif ch == 2:
        read_note.read_notes()
    elif ch == 3:
        remove_note.remove_note()
    elif ch == 4:
        print("До побачення")
        break
    else:
        print("Такого варіанту не існує")