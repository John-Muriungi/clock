from time import strftime
import tkinter as tk
from tkinter.ttk import *


root = tk.Tk()

root. title('Clock')


def thetime():
    string = strftime('%H:%M:%S %p')
    Label.config(text=string)
    Label.after(1000, thetime)


Label = tk.Label(root, font=('Arial', 70),
                 background='black', foreground='pink')
Label.pack(anchor='center')

thetime()
root.mainloop()
