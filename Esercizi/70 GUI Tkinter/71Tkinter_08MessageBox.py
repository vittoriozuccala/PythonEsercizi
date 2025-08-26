import tkinter as tk
from  PIL import Image, ImageTk
from tkinter import messagebox      # Bisogna aggiungerlo specificatamente...
import os

root = tk.Tk()  # Creo una root
root.title("Frames")
# icona è un png con estensione ICO 7x7 o 32x32 o 64x64
root.iconbitmap('Images\\favicon.ico')


def popup() -> None:
    response = messagebox.askyesno(title="Prova", message="Messaggio di prova")
    global testo
    testo.set(response)
    # Metti command
    # showinfo
    # showwarning
    # showerror
    # askquestion
    # askokcancel
    # askretrycancel
    # askyesno
    # askyesnocancel
    '''
    ymbolic names of buttons:

tkinter.messagebox.ABORT = 'abort'
tkinter.messagebox.RETRY = 'retry'
tkinter.messagebox.IGNORE = 'ignore'
tkinter.messagebox.OK = 'ok'
tkinter.messagebox.CANCEL = 'cancel'
tkinter.messagebox.YES = 'yes'
tkinter.messagebox.NO = 'no'
Predefined sets of buttons:

tkinter.messagebox.ABORTRETRYIGNORE = 'abortretryignore'
Displays three buttons whose symbolic names are ABORT, RETRY and IGNORE.

tkinter.messagebox.OK = 'ok'
Displays one button whose symbolic name is OK.

tkinter.messagebox.OKCANCEL = 'okcancel'
Displays two buttons whose symbolic names are OK and CANCEL.

tkinter.messagebox.RETRYCANCEL = 'retrycancel'
Displays two buttons whose symbolic names are RETRY and CANCEL.

tkinter.messagebox.YESNO = 'yesno'
Displays two buttons whose symbolic names are YES and NO.

tkinter.messagebox.YESNOCANCEL = 'yesnocancel'
Displays three buttons whose symbolic names are YES, NO and CANCEL.
    '''

testo = tk.StringVar()
testo.set("Prova")

myLabel = tk.Label(root, textvariable=testo).pack()

tk.Button(root, text="Popup", command=popup).pack()


root.mainloop()

