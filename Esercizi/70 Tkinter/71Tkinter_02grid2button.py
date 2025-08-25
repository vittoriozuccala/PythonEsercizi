import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

root = tk.CTk()  # Creo una root

myLabel1 = tk.CTkLabel(root, text="Hello World")
myLabel2 = tk.CTkLabel(root, text="Mio nome è Vittorio")

# Bottone disabilitato: state="disabled"
def ClickButton():
    myLabel = tk.CTkLabel(root, text="Ho cliccato!!", fg="red")
    myLabel.grid(row=2,column=0)

myButton = tk.CTkButton(master=root, text="Premi", width=50, height=10, hover_color="blue",  command=ClickButton) # NON USARE LE PARENTESI X FUNZIONE O LA ESEGUE SUBITO

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=2, column=1)


root.mainloop()

