import tkinter as tk
from  PIL import Image, ImageTk
import os

root = tk.Tk()  # Creo una root
root.title("Simple Image Viewer")

# icona è un png con estensione ICO 7x7 o 32x32 o 64x64
root.iconbitmap('Images\\favicon.ico')


numeroTot: int = 0 

def listaFiles(numero: int ) -> str:
    global numeroTot

    dir = "Images"
    contents = os.listdir(dir)
    lunghezza = len(contents)-1
    numeroFin = numeroTot + numero
    print(lunghezza)
    if numeroFin >= lunghezza:
        numeroTot = lunghezza
    elif numeroFin <=0:
        numeroTot = 0
    else:
        numeroTot = numeroFin
    
    print("numeroFin:",numeroFin, "numeroTot:", numeroTot, "numero:", numero)

    fileImg =  dir + "\\" + contents[numeroTot] 
    
    return fileImg


def buttonDirection(numero: int) -> None:
    global myImg
    global label 
    label.grid_forget()     # IMPORTANTE

    myImg = ImageTk.PhotoImage(Image.open(listaFiles(numero)))
    label = tk.Label(root, image=myImg)
    label.grid(row=0, column=0, columnspan=3)

myImg = ImageTk.PhotoImage(Image.open(listaFiles(0)))
label = tk.Label(root, image=myImg)


buttonLeft =  tk.Button(root, text="<<", command=lambda: buttonDirection(-1))
buttonQuit =  tk.Button(root, text="Exit Program!", command=root.quit)
buttonRight = tk.Button(root, text=">>", command=lambda: buttonDirection(1))


label.grid(row=0, column=0, columnspan=3)
buttonLeft.grid(row=1, column=0)
buttonQuit.grid(row=1, column=1)
buttonRight.grid(row=1, column=2)


root.mainloop()

