#To make a tkinter window scrollable

#First__we make a tkinter window
from tkinter import *

win=Tk()
win.title("IDENTITY CARD GENRATOR")
win.geometry("580x1000")     
win.resizable(0,0)

#Second__we add a frame it will mainframe 
mainframe=Frame(win)
mainframe.pack(expand=YES,fill=BOTH)

#Third__Create a Canvas widget, and place it inside your main frame.
#This canvas will act as the scrollable area.
canvas=Canvas(mainframe)
canvas.pack(side="left",fill="both",expand=True)


#fourth__Create another Frame widget  and place it inside the canvas.
#This inner frame will hold all the widgets you want to display and scroll. 
#(this will be the content frame)
innerframe=Frame(canvas)
innerframe.pack(expand=YES,fill=BOTH)


#fifth__Create Scrollbar widgets (one for vertical and one for horizontal if needed).
"""
v_scroll = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
h_scroll = tk.Scrollbar(frame, orient='horizontal', command=canvas.xview)

Pack the scrollbars next to the canvas (e.g., on the right for vertical, and bottom for horizontal).
v_scroll.pack(side="right", fill="y")
h_scroll.pack(side="bottom", fill="x")
"""
v_scroll=Scrollbar(mainframe,command=canvas.yview)
v_scroll.pack(side=RIGHT,fill="y")


#Sixth__Configure Scrollbars:
"""
Link the scrollbars to the canvas
using the yscrollcommand and xscrollcommand options
#canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
"""
canvas.configure(yscrollcommand=v_scroll.set)



#Seventh__Configure Canvas Scroll Region:   
"""
After adding all the widgets to inner_frame, update canvas's
scroll region to match the size of the inner_frame.
This allows the scrollbars to function correctly.
"""
innerframe.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


#Eight__Create Window in Canvas:
"create a window within the canvas to hold the inner_frame. "
canvas.create_window((0, 0), window=innerframe,anchor="w")


"This setup ensures that the inner_frame and its contents can be scrolled within the canvas using the scrollbars."


win.mainloop()

