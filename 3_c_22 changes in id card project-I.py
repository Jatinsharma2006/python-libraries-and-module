from tkinter import*
from tkinter import messagebox,ttk

#
import pyqrcode,os
import matplotlib.image as mi
import matplotlib.pyplot as plt
#

win=Tk()
win.title("hello")
win.geometry("700x650")
win.resizable(0,0)
win.config(bg="lime")
win.iconbitmap("techdev.ico")

#
img=PhotoImage(file="abc.png")
#

name=StringVar(value="")
gender=StringVar(value="M")             
married=BooleanVar(value=False)
age=IntVar(value=18)
city=StringVar(value="Bhopal")
address=StringVar(value="")

#
def resultClick():
    #msg+=
    msg='<<<<<<<<.........IDENTITY CARD.........>>>>>>>>'
    if gender.get()=='M':
        prefix='Mr.'
    else:
        prefix='Ms.'
    msg+=f'\n{prefix}+{name.get().title()}'
    msg+='\nAge'+str(age.get())
    msg+='\nGender'+gender.get()
    msg+='\nCity'+city.get()
    msg+='\nAddress'+txtAddress.get(0.0,END).strip()

    txtResult.delete(0.0,END)
    txtResult.insert(0.0,msg)

    btnQRCode.invoke()            #Programmatically Click Button
    messagebox.showinfo("ID CARD",msg)

def qrcodeClick():
    data=txtResult.get(0.0,END)
    if len(data)==0:
        messagebox.showerror('ERROR','NO DATA FOUND')
        return                       #Terminate fn
    #Otherwise
    url=pyqrcode.create(data)        #One line to create qr code
    filename=name.get()+str(age.get())+".png"
    url.png(filename,scale=2)        #Now save the image
    print(f'QR Code genrated at {os.getcwd()}/{filename}')
    img2=PhotoImage(file=filename)
    lblQRCode.config(image=img2)

    image=mi.imread(filename)#Read image
    plt.imshow(image) #show image
    plt.show()

def clearClick():
    name.set("")
    gender.set('M')
    married.set(value=False)
    age.set(value=18)
    city.set(value='Bhopal')
    txtAddress.delete(0.0,END)
    txtResult.delete(0.0,END)
    lblQRCode.config(image=img)
#




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
btnResult=Button(frame1,text="SHOW RESULT",command=resultClick)
btnResult.grid(row=6,column=0,columnspan=2)



#
#QR Code button
btnQRCode=Button(frame1,text="GENRATE QR CODE",command=qrcodeClick)
btnQRCode.grid(row=6,column=1,columnspan=2)
#Clear button
btnClear=Button(frame1,text="CLEAR",command=clearClick)
btnClear.grid(row=6,column=2,columnspan=2)
#


frame2=Frame(win)
frame2.pack(anchor="n",expand=True,fill=BOTH)
Label(frame2,text="RESULT IS").grid(row=0,column=0)
txtResult=Text(frame2,width=70,height=13,state="normal")
txtResult.grid(row=1,column=1,columnspan=3)

#
lblQRCode=Label(frame2,image=img)
lblQRCode.grid(row=1,column=3,columnspan=2,sticky='n')
#

win.mainloop()
