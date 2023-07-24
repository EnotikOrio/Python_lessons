import tkinter as tk

def change_color(color):
    label.config(text=color, bg=color)

window = tk.Tk()
window.geometry('400x200')
window.title('ПР_15: Світлофор_ПІБ')

green_button = tk.Radiobutton(window, text='Зелений', value='green', command=lambda: change_color('green'))
yellow_button = tk.Radiobutton(window, text='Жовтий', value='yellow', command=lambda: change_color('yellow'))
red_button = tk.Radiobutton(window, text='Червоний', value='red', command=lambda: change_color('red'))

green_button.pack()
yellow_button.pack()
red_button.pack()

label = tk.Label(window, text='Колір')
label.pack()

window.mainloop()
