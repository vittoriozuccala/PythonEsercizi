import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

root = tk.CTk()  # Creo una root

myLabel = tk.CTkLabel(root, text="Hello World")
myLabel.pack()      #Showinf into the screen


root.mainloop()

