import tkinter as tk

root = tk.Tk()  # Creo una root

myLabel1 = tk.Label(root, text="Hello World")
myLabel2 = tk.Label(root, text="Inserisci il tuo nome: ")
myInput = tk.Entry(width=50, fg="blue", borderwidth=4)
myInput.insert(0, "Inserisci nome")     #Serve per un popup nel input

# Bottone disabilitato: state="disabled"
def ClickButton():

    testo = "Hai inserito: " + myInput.get()
    myLabel = tk.Label(root, text=testo, fg="red")
    myLabel.grid(row=2,column=0)

myButton = tk.Button(root, text="Enter Name", padx=50, pady=10, fg="blue", command=ClickButton) # NON USARE LE PARENTESI X FUNZIONE O LA ESEGUE SUBITO

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myInput.grid(row=1,column=1)
myButton.grid(row=2, column=1)


root.mainloop()

