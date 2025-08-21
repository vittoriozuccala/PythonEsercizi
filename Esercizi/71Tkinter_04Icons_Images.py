import tkinter as tk
from  PIL import Image, ImageTk

root = tk.Tk()  # Creo una root
root.title("Simple Code")

# icona è un png con estensione ICO 7x7 o 32x32 o 64x64
root.iconbitmap('Images\\favicon.ico')


myImg = ImageTk.PhotoImage(Image.open('Images\\nature.gif'))
label = tk.Label(root, image=myImg)
label.pack()


buttonQuit = tk.Button(root, text="Exit Program!", command=root.quit)
buttonQuit.pack()


root.mainloop()

