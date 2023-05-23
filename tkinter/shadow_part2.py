from tkinter import *




root = Tk()
root.geometry("500x500")

frame1   = Frame(root , height = 300  ,width=300 , background='grey')
frame2  = Frame(root , height= 300 , width  =300 , background='red')


frame1.place(x = 24 ,  y = 24  )
frame2.place(x = 20 , y = 20)




root.mainloop()