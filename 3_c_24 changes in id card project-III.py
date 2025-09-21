def genrateHTML(name1,age1,gender1,city1,address1,married1,photo1,qrcode1,mobile1,birthdate1,bloodgroup1,course1):
    html=f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <title>IDENTITY CARD</title>
        <!--BOOTSTRAP CSS CDN-->
        <link href="bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="style1.css">
    </head>
    <body>
        <div class="container">
        
        <div class="id-card">
            <!--Collage Name and Logo-->
            
            <div class="ok">
                <img id=logo src="abc.png" alt="GHACC">
                <h3 id="collagename">
                   <b>GOVT HAMIDIYA ARTS AND COMMERCE COLLAGE</b>
                   <p id="collageinfo"> Hathi Khana,Budwara,Bhopal,462001(MP)<br/>
                    Contact 0755-2660081,2660447 
                   </p>
                </h3>
            </div>

            <!--DOUBLE HORIZONTAL LINE-->
            <hr class="double-line">
            <!--STUDENT INFO-->
            <div class="ok">
                <div class="student-info"><b>
                    NAME:{name1}<br/>
                    COURSE:{course1}<br/>         BIRTHDATE:{birthdate1}<br/>
                    AGE:{age1}<br/>               GENDER:{gender1}<br/>
                    MARITAL STATUS:{married1}<br/>ADDRESS:{address1}<br/>
                    MOBILE:{mobile1}<br/>         BLOOD GROUP:{bloodgroup1}<br/>
                    </b>
                </div>
                <div class="profile-photo-qrcode">
                    <img id=images src="{photo1}" alt="Student Photo"/>
                    <img id=images src="{qrcode1}"alt="QR CODE"/>
                </div>
            </div>
        </div>
    </div>
    
    <div class="d-flex justify-content-center">
        <button class="btn btn-primary text-center" type="button" onclick="window.print()">PRINT</button>
        <button class="btn btn-primary text-center" type="button" onclick="genratePDF()">Generate PDF</button>
    </div>
    <!--BOOTSTRAP JS CDN-->
    <script src="bootstrap.bundle.min.js"></script>
    <script src="jquery-3.6.4.min.js"></script>
    </body>
    </html>
    """
    return html



"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

from tkinter import*
from tkinter import messagebox,ttk
import pyqrcode,os
import matplotlib.image as mi
import matplotlib.pyplot as plt
import webbrowser
import tempfile
from tkinterweb import HtmlFrame
###
from tkinter.messagebox import askyesno
from tkinter.simpledialog import askstring
from weasyprint import HTML
###

win=Tk()
win.title("IDENTITY CARD GENRATOR")
win.geometry("900x1000")     
win.resizable(0,0)
win.config(bg="lime")      
win.iconbitmap("techdev.ico")


name=StringVar(value="")
gender=StringVar(value="Male")             
married=BooleanVar(value=False)
age=IntVar(value=18)
city=StringVar(value="Bhopal")
address=StringVar(value="")
bloodgroup=StringVar(value="B+")
birthdate=StringVar(value="01-Jan-2006")
mobile=StringVar(value="3054120505")
course=StringVar(value="BCA")
img=PhotoImage(file="abc.png")



def resultClick():
    msg='<<<<<<<<.........IDENTITY CARD.........>>>>>>>>'
    if gender.get()=='Male':
        prefix='Mr.'
    else:
        prefix='Ms.'
    msg+=f'\n{prefix}{name.get().title()}'
    msg+='\nAge'+str(age.get())
    msg+='\nGender'+gender.get()
    msg+='\nCity'+city.get()
    msg+='\nAddress'+txtAddress.get(0.0,END).strip()

    txtResult.delete(0.0,END)
    txtResult.insert(0.0,msg)

    btnQRCode.invoke()      
    messagebox.showinfo("ID CARD",msg)  
    
    btnPDF.config(state="normal")
    btnAudio.config(state="normal")
    btnSave.config(state="normal")
    btnHindi.config(state="normal")
    btnHTML.config(state="normal")

     
def qrcodeClick():
    data=txtResult.get(0.0,END)
    if len(data)==0:
        messagebox.showerror('ERROR','NO DATA FOUND')
        return                       
    #Otherwise
    url=pyqrcode.create(data)        
    filename=name.get()+str(age.get())+".png"
    url.png(filename,scale=2)        
    print(f'QR Code genrated at {os.getcwd()}/{filename}')
    img2=PhotoImage(file=filename)
    lblQRCode.config(image=img2)

    image=mi.imread(filename)
    plt.imshow(image) 
    plt.show()
    
def clearClick():
    name.set("")
    gender.set('Male')
    married.set(value=False)
    age.set(value=18)
    city.set(value='Bhopal')
    txtAddress.delete(0.0,END)
    txtResult.delete(0.0,END)
    lblQRCode.config(image=img)
    btnHTML.config(state="disabled")
    btnPDF.config(state="disabled")
    btnAudio.config(state="disabled")
    btnSave.config(state="disabled")
    btnHindi.config(state="disabled")
###    
def pdfClick():
    filename=name.get()+"_"+str(age.get())
    htmlfile=filename+".html"
    if not os.path.exists(htmlfile):
        messagebox.showerror("file Not Found",f"Sorry {filename} File Not Found")
        return
    #Otherwise
    pdffile=filename+".pdf"
    HTML(htmlfile).write_pdf(pdffile)    #weasypdf library
    messagebox.showinfo("Saved",f'PDF saved at {os.getcwd()}/{filename}')
###    
    

def hindiClick():
    pass
###
def saveClick():
    confirm=askyesno(title="confirmation",message="Are you sure to SAVE it?")
    if not confirm:
        return
    #Otherwise,collect and save data
    name1=name.get().title()
    age1=str(age.get())
    gender1=gender.get()
    city1=city.get()
    address1=txtAddress.get(0.0,END).strip()
    mobile1=mobile.get().strip()
    birthdate1=birthdate.get()
    bloodgroup1=bloodgroup.get()
    course1=course.get()

    married1="Married"if married.get() else"Single"

    photo1=name.get()+course.get()+".png"
    qrcode1=name.get()+str(age1.get())+".png"

    data=[name1,age1,gender1,city1,address1,married1,photo1,qrcode1,mobile1,birthdate1,bloodgroup1,course1]

    record=",".join(data)+"\n"

    with open('record.csv','a')as file:
        file.write(record)
        messagebox.showinfo('Record Saved',f'Record{name1} saved successfully')
###   

def audioClick():
    pass


def htmlClick():
    name1=name.get().title()
    age1=age.get()
    gender1=gender.get()
    city1=city.get()
    address1=txtAddress.get(0.0,END).strip()
    mobile1=mobile.get().strip()
    birthdate1=birthdate.get()
    bloodgroup1=bloodgroup.get()
    course1=course.get()

    married1="Married"if married.get() else"Single"

    photo1=name.get()+course.get()+".png"
    qrcode1=name.get()+str(age1)+".png"

    
    data=[name1,age1,gender1,city1,address1,married1,photo1,qrcode1,mobile1,birthdate1,bloodgroup1,course1]
    html=genrateHTML(*data)
    frame4.load_html(html)
    filename=name1+"_"+str(age1)+".html"
    with open(filename,"w",encoding="utf-8")as file:
        file.write(html)
    webbrowser.open(f"file://{os.path.abspath(filename)}")
    
    

"""###########################################################"""
##frame1
frame1=LabelFrame(win,text="Enter Your Information")
frame1.pack(fill=X,expand=True, anchor="n")


lblName=Label(frame1,text="ENTER NAME:")
lblName.grid(row=0,column=0)

txtName=Entry(frame1,width=20,textvariable=name)
txtName.grid(row=0,column=1,columnspan=2)


#gender radio button
Label(frame1,text="SELECT GENDER").grid(row=1,column=0)
#for male
rdoMale=Radiobutton(frame1,value="Male",text="Male",variable=gender)
rdoMale.select()
rdoMale.grid(row=1,column=1)
#for female
rdoFemale=Radiobutton(frame1,value="Female",text="Female",variable=gender)
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


#QR Code button
btnQRCode=Button(frame1,text="GENRATE QR CODE",command=qrcodeClick)
btnQRCode.grid(row=6,column=1,columnspan=2)


#Clear button
btnClear=Button(frame1,text="CLEAR",command=clearClick)
btnClear.grid(row=6,column=2,columnspan=2)
"""###########################################################"""



"""###########################################################"""
##frame2
frame2=Frame(win)
frame2.pack(anchor="n",expand=True,fill=BOTH)

Label(frame2,text="RESULT IS").grid(row=0,column=0)

#RESULT TEXT BOX
txtResult=Text(frame2,width=70,height=13,state="normal")
txtResult.grid(row=1,column=1,columnspan=3)

#DISPLAYING QR CODE LABEL
lblQRCode=Label(frame2,image=img)
lblQRCode.grid(row=1,column=3,columnspan=2,sticky='n')
"""###########################################################"""




"""###########################################################"""
##frame3
frame3=Frame(frame2)
frame3.grid(row=2,column=0,columnspan=4)

#HTML BUTTON
btnHTML=Button(frame3,text="GENRATE HTML",command=htmlClick)
btnHTML.grid(row=0,column=0,columnspan=2,sticky='n')

#PDF BUTTON
btnPDF=Button(frame3,text="GENRATE PDF",command=pdfClick)
btnPDF.grid(row=0,column=4,columnspan=2,sticky='n')

#SAVE BUTTON
btnSave=Button(frame3,text="SAVE",command=saveClick)
btnSave.grid(row=0,column=8,columnspan=2,sticky='n')

#HINDI button
btnHindi=Button(frame3,text="Language change",command=hindiClick)
btnHindi.grid(row=0,column=12,columnspan=2)

#Audio button
btnAudio=Button(frame3,text="AUDIO",command=audioClick)
btnAudio.grid(row=0,column=20,columnspan=2)
"""###########################################################"""




"""###########################################################"""
##frame 4
frame4=HtmlFrame(win,horizontal_scrollbar="auto")
frame4.pack(anchor="n",expand=True,fill=BOTH)
html="<b>IDENTITY CARD APP</b>"
frame4.load_html(html)
"""###########################################################"""

win.mainloop()
