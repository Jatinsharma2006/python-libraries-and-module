#Color chooser in tkinter

from tkinter import *
from tkinter import colorchooser

def choose_color():
    color_code = colorchooser.askcolor(title="Choose a color")

    if color_code:
        label.config(text=f"Selected Color:{color_code[1]}",bg=color_code[1])

win = Tk()
win.title("COLOR CHOOSER EXAMPLE")


button= Button(win,text="Show Selection", command=choose_color)
button.pack(pady=20)


label=Label(win,text="No color selected")
label.pack(pady=20)

win.mainloop()
