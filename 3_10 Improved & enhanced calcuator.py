from tkinter import*
from tkinter import messagebox


win =Tk()
win.title("lets Calculate")
win.geometry("400x600")
win.configure(bg="blue")

main_color="blue"
led_color="#66ff00"
led_text="#FF5733"
text=StringVar(value="helloo")

buttons=[
    ("7",'8','9','/'),
    ("4",'5','6','*'),
    ("1",'2','3','-'),
    ("c",'0','=','+')]

decorate={"font":("Arial",18),\
          "bg":"#0A0A0A","fg":"white", \
          "activebackground":"#c1c1d1",\
          "activeforeground":"#000000",\
          'relief':"ridge",'bd':2}

entry=Entry(win,font=("Seven Segment",30,"bold"),\
            justify="right",textvariable=text, \
            bd=8,relief="ridge",bg=led_color,fg=led_text)
entry.pack(side=TOP,fill=BOTH,ipadx=4,ipady=4,padx=6,pady=6) 


def buttonClick(btn):
    current=text.get()
    if btn=="c": text.set('')
    elif btn=="=":
        try:
            result=eval(current)
            text.set(result)
        except Exception as e:
            messagebox.showerror("Error","Invalid Input")
    elif current=="helloo":
        text.set(btn)
    else:
        text.set(current+btn)



button_frame=Frame(win,bg=main_color)
button_frame.pack(side=TOP,fill=BOTH,expand=True)

for row in buttons:
    button_row=Frame(button_frame,bg=main_color)
    button_row.pack(side=TOP,fill=BOTH,expand=True)
    for button in row:
        btn=Button(button_row,text=button,command=lambda b=button:buttonClick(b),**decorate)
        btn.pack(side=LEFT,fill=BOTH,expand=True,padx=1,pady=1)



win.mainloop()









