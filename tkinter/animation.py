import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x300')

# Define a custom style for the button
style = ttk.Style()
style.configure('Animated.TButton', font=('Arial', 12), foreground='white', background='blue', borderwidth=0)

# Create the button using the custom style
button = ttk.Button(root, text='Click me!', style='Animated.TButton')
button.pack()

# Define a function to animate the button
def animate_button():
    current_bg = style.lookup('Animated.TButton', 'background')
    if current_bg == 'blue':
        style.configure('Animated.TButton', background='green')
    else:
        style.configure('Animated.TButton', background='blue')
    button.after(500, animate_button)  # Call this function again after 500 milliseconds
    button.after(100 , lambda : print("Hello world"))

# Start animating the button
animate_button()

root.mainloop()
