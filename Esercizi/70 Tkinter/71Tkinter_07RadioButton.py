import tkinter as tk
from  PIL import Image, ImageTk
import os

root = tk.Tk()  # Creo una root
root.title("Frames")
# icona è un png con estensione ICO 7x7 o 32x32 o 64x64
root.iconbitmap('Images\\favicon.ico')

pizza = tk.StringVar()
pizza.set("Peperoni")

def clicked(value: str):
    myLabel = tk.Label(root, text=pizza.get())
    myLabel.pack()    

MODES = [
    ("Peperoni","Peperoni"),
    ("Cipolle","Cipolle"),
    ("Funghi","Funghi"),
    ("Gorgonzola","Gorgonzola"),
]

for ingrediente, valore in MODES:
    tk.Radiobutton(root, text=ingrediente, value=valore, variable=pizza, command=lambda: clicked(valore)).pack(anchor=tk.W)



myLabel = tk.Label(root, text=pizza.get())
myLabel.pack()


root.mainloop()

