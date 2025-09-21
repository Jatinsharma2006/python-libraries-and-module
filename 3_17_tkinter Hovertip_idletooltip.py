"Using tooltip from idlelib (comes with Python)"
#from idlelib.tooltip import Hovertip
#hover_delay is in milliseconds (e.g., 1000 ms = 1 sec).

from tkinter import *
from idlelib.tooltip import Hovertip
#Standard tooltip from idlelib

win = Tk()
win.geometry("400x300")
win.title("Tool tip text")

b1 = Button(win, text="Save")
b1.pack(pady=10)

b2 = Button(win, text="Open")
b2.pack(pady=10)

Hovertip(b1, "To Save the Data to a file", hover_delay=1000)
Hovertip(b2, "To Open existing file", hover_delay=1000)

win.mainloop()

