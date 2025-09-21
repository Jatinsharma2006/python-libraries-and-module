from tkinter import*
from tkinter import messagebox,ttk
win=Tk()
win.title("hello")
win.geometry("700x650")
win.resizable(0,0)
win.config(bg="lime")
win.iconbitmap("")


name=StringVar(value="")
gender=StringVar(value="M")             
married=BooleanVar(value=False)
age=IntVar(value=18)
city=StringVar(value="Bhopal")
address=StringVar(value="")



frame1=LabelFrame(win,text="Enter Your Information")
frame1.pack(fill=X,expand=True, anchor="n")

lblName=Label(frame1,text="ENTER NAME:")
lblName.grid(row=0,column=0)

txtName=Entry(frame1,width=20,textvariable=name)
txtName.grid(row=0,column=1,columnspan=2)



#gender radio button
Label(frame1,text="SELECT GENDER").grid(row=1,column=0)
#for male
rdoMale=Radiobutton(frame1,value="M",text="Male",variable=gender)
rdoMale.select()
rdoMale.grid(row=1,column=1)
#for female
rdoFemale=Radiobutton(frame1,value="F",text="Female",variable=gender)
rdoFemale.deselect()
rdoFemale.grid(row=1,column=2)



#checkbutton for married or not
Label(frame1,text="ARE YOU MARRIED?").grid(row=2,column=0)
chkMarried=Checkbutton(frame1,variable=married,offvalue=False,onvalue=True)
chkMarried.grid(row=2,column=1,sticky="w")




#age spinbox
Label(frame1,text="ENTER AGE").grid(row=3,column=0)
spiAge=Spinbox(frame1,textvariable=age,from_=1,to=100)
spiAge.grid(row=3,column=1,columnspan=2)



#city combobox
Label(frame1,text="SELECT CITY OF YOUR BIRTH").grid(row=4,column=0)
cities=["Bhopal","Ujjain","Indore"]
cmbCity=ttk.Combobox(frame1,value=cities,textvariable=city)
cmbCity.grid(row=4,column=1,columnspan=2)



#address  multiline text
Label(frame1,text="ENTER ADDRESS").grid(row=5,column=0)
txtAddress=Text(frame1,width=50,height=5)
txtAddress.grid(row=5,column=1,columnspan=2)



#result button
btnResult=Button(frame1,text="SHOW RESULT")#,command=resultClick)
btnResult.grid(row=6,column=0,columnspan=2)


frame2=Frame(win)
frame2.pack(anchor="n",expand=True,fill=BOTH)
Label(frame2,text="RESULT IS").grid(row=0,column=0)
txtResult=Text(frame2,width=50,height=5,state="normal")
txtResult.grid(row=1,column=1,columnspan=2)








win.mainloop()
