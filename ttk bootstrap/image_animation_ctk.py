import tkinter as tk

from tkinter import ttk
import customtkinter as ctk 
from PIL import Image ,  ImageTk


root  = tk.Tk()

root.geometry('200x200')

other  = Image.open(r'ttk bootstrap\Motospeed Learning.PNG')
other_re = other.resize((15,15))
oth_fin = ImageTk.PhotoImage(other_re)




# main_btn  = tk.Button(root, text="Hello World" , image=oth_fin ).pack()
other_btn  = ctk.CTkButton(root , text="Hello World" , image=oth_fin , compound='right').pack()



root.mainloop()