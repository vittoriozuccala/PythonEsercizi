import tkinter as tk

root = tk.Tk()  # Creo una root
root.title("Simple Calculator")

def buttonClik(numero: int) -> None:
    lunghezza = len(e.get())+1
    if numero == 10:
        e.insert(lunghezza,"+")
    elif numero == 11:
        e.insert(lunghezza,"-")
    elif numero == 12:
        e.insert(lunghezza,"/")
    elif numero == 13:
        e.insert(lunghezza,"*")
    else:
        e.insert(lunghezza,numero)
    
def buttonCls() -> None:
    e.delete(0,tk.END)

def buttonEq() -> None:
    operazione = e.get()
    e.delete(0,tk.END)
    e.insert(0,eval(operazione))

e = tk.Entry(root, width=50, borderwidth=5)
button1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: buttonClik(1))
button2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: buttonClik(2))
button3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: buttonClik(3))
button4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: buttonClik(4))
button5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: buttonClik(5))
button6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: buttonClik(6))
button7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: buttonClik(7))
button8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: buttonClik(8))
button9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: buttonClik(9))
button0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: buttonClik(0))

buttonPlus = tk.Button(root, text="+", padx=40, pady=20,  command=lambda: buttonClik(10))
buttonMinus = tk.Button(root, text="-", padx=40, pady=20,  command=lambda: buttonClik(11))
buttonDivide = tk.Button(root, text="/", padx=40, pady=20,  command=lambda: buttonClik(12))
buttonMultiply = tk.Button(root, text="*", padx=40, pady=20,  command=lambda: buttonClik(13))

buttonEqual = tk.Button(root, text="=", padx=90, pady=20,  command=buttonEq)
buttonClear = tk.Button(root, text="Clear", padx=90, pady=20,  command=buttonCls)


e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)   # columnspane per tre colonne
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=0)

buttonPlus.grid(row=1,column=3)
buttonMinus.grid(row=2,column=3)
buttonDivide.grid(row=3,column=3)
buttonMultiply.grid(row=4,column=3)

buttonEqual.grid(row=4, column=1, columnspan=2)
buttonClear.grid(row=5, column=1, columnspan=2)




root.mainloop()

