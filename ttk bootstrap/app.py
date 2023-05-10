import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *



root  = tk.Tk()

main_button  = ttk.Button(root , text="Hello World").pack()

meter_widet = ttk.Menubutton(root).pack()


root.mainloop()
