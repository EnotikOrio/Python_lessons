import tkinter as tk

def button1_clicked():
    window.config(bg='#ADD8E6')
    label.config(text='Ви натиснули на Кнопку 1')

def button2_clicked():
    window.config(bg='yellow')
    label.config(text='Ви натиснули на Кнопку 2')

window = tk.Tk()
window.title('ПР_14: Іванов І.І.')
window.geometry('600x400')
window.resizable(False, False)

button1 = tk.Button(window, text='Кнопка № 1', command=button1_clicked)
button1.place(x=100, y=50)

button2 = tk.Button(window, text='Кнопка № 2', command=button2_clicked)
button2.place(x=300, y=50)

label = tk.Label(window, text='')
label.place(x=100, y=100)

window.mainloop()
