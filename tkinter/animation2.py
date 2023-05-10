import tkinter as tk

class AnimatedButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.current_bg = 'blue'
        self.animate()

    def animate(self):
        if self.current_bg == 'blue':
            self.configure(background='green')
            self.current_bg = 'green'
        else:
            self.configure(background='blue')
            self.current_bg = 'blue'
        self.after(500, self.animate)

root = tk.Tk()

# Create an animated button
button = AnimatedButton(root, text='Click me!', font=('Arial', 12), foreground='white', background='blue', borderwidth=0)
button.pack()

root.mainloop()
