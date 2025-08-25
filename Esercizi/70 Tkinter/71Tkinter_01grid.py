import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

root = tk.CTk()  # Creo una root

myLabel1 = tk.CTkLabel(root, text="Hello World")
myLabel2 = tk.CTkLabel(root, text="Mio nome è Vittorio")
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)


root.mainloop()

