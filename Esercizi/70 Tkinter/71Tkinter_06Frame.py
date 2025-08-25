import tkinter as tk
from  PIL import Image, ImageTk
import os

root = tk.Tk()  # Creo una root
root.title("Frames")
# icona è un png con estensione ICO 7x7 o 32x32 o 64x64
root.iconbitmap('Images\\favicon.ico')


frame = tk.LabelFrame(root, text="First Frame", padx=5, pady=5)
frame.pack()

b = tk.Button(frame,text="Do not click")
b.pack()

b2 = tk.Button(root,text="Do not click")
b2.pack()

root.mainloop()

