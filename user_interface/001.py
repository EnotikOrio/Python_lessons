import tkinter as tk

def on_button_1_click():
    s1 = entr_1.get()
    print("Привіт " + s1)
    lbl_2.config(text="Hello " + s1, width=len(s1) + 3)

window = tk.Tk()
window.title("Calculator V.0.1")
window.geometry("800x600+100+100")
window.resizable(width=False, height=False)
window.configure(bg="purple")
lbl_1 = tk.Label(window, text="Введіть текст:" )
lbl_1.pack()
lbl_2 = tk.Label(window, text="", width="23")
lbl_2.pack()
entr_1 = tk.Entry(window)
entr_1.pack()
button_1 = tk.Button(window, text="Натисни на мене!", command=on_button_1_click)
button_1.pack()

window.mainloop()