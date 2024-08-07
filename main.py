import tkinter as tk

from tkinter import *
from tkinter import messagebox

def add_variation():
    k = first_input.get()
    messagebox.showinfo('Project', f'Вариант {k} добавлен')

window = Tk()
window.title("Выбор лучшего варианта")

frame = Frame(
    window,
    padx = 10,
    pady = 10
)
frame.pack(expand=True)

first_letter = Label(
    frame,
    text = "Введите вариант: "
)
first_letter.grid(row = 3, column = 1)

first_input = Entry(
    frame,
)
first_input.grid(row = 3, column = 2)

first_button = Button(
    frame,
    text = "Добавить вариант",
    command = add_variation
)
first_button.grid(row = 5, column = 2)

window.geometry('400x300')
window.mainloop()