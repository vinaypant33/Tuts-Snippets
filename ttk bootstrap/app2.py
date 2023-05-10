from tkinter import * 

import ttkbootstrap as ttbk

root  = Tk()



frm = Frame(root).pack()


lab = Label(frm , text="u'\u00AC'")
lab.pack()
btn  = Button(frm , text=" Click ME " ,command=  lambda :  root.after(100 , pp)).pack()



mtr = ttbk.Meter(root ,interactive=True).pack()

def pp():
    lab.pack_forget()


root.mainloop()