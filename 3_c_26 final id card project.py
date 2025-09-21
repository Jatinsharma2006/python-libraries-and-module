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
from tkinter.messagebox import askyesno
from tkinter.simpledialog import askstring
from tkinter import filedialog

import matplotlib.image as mi
import matplotlib.pyplot as plt
import pyqrcode,os
import webbrowser
import tempfile
#pip install playsound==1.2.2
import playsound

from tkinterweb import HtmlFrame
from weasyprint import HTML
from datetime import datetime
from googletrans import Translator,LANGUAGES
from gtts import gTTS


win=Tk()
win.title("IDENTITY CARD GENRATOR")
win.geometry("580x1000")     
win.resizable(0,0)
win.iconbitmap("techdev.ico")

mainframe=Frame(win)
mainframe.pack(expand=YES,fill=BOTH)

canvas=Canvas(mainframe)
canvas.pack(side="left",fill="both",expand=True)

innerframe=Frame(canvas)
innerframe.pack(expand=YES,fill=BOTH)

v_scroll=Scrollbar(mainframe,command=canvas.yview)
v_scroll.pack(side=RIGHT,fill="y")


name=StringVar(value="")
gender=StringVar(value="Male")             
married=BooleanVar(value=False)
age=IntVar(value=18)
city=StringVar(value="BHOPAL")
bloodgroup=StringVar(value="B+")
birthdate=StringVar(value="01-01-2006")
mobile=StringVar(value="3054120505")
course=StringVar(value="BCA")
img=PhotoImage(file="abc.png")

lang_names=["English",'Hindi','Punjabi','Marathi','Bengali']
src_lang=StringVar(value="English")
tgt_lang=StringVar(value="Hindi")


def validateData():
    name1=name.get().strip()
    address1=txtAddress.get(0.0,END).strip()
    mobile1=mobile.get().strip()
    birthdate1=birthdate.get()
    msg=""

    if len(name1)<2 or not name1.isalpha():
        msg+="\nName should be more than 2 characters and should be alphabets only"

    if len(mobile1)<10 or not mobile1.isdigit():
        msg+="\nMobile Number should be of atleast 10 Digits"

    if len(birthdate1)<8 or not birthdate1.replace("-","").isdigit():
        msg+="\nBirthdate should be of atleast 8 Digits and should be in dd-mm-yy"
        return msg
    
    #Compute Age and birthdate
    birthday=datetime.strptime(birthdate1,"%d-%m-%Y")
    age1=(datetime.today()-birthday).days//365
    age.set(age1)
    photo1=name.get()+course.get()+".png"
    if not os.path.exists(photo1):
        msg+=f'\nPhoto{photo1} not found'
        return
    
def resultClick():
    validateData()
    if gender.get()=='Male':
        prefix='Mr.'
    else:
        if married.get()==True:
            prefix="Mrs."
        else:
            prefix='Ms.'
        
    msg='<<<<<<<<.........IDENTITY CARD.........>>>>>>>>'
    msg+=f'\nNAME:  {prefix}{name.get().title()}'
    msg+='\nBIRTHDATE:  '+str(birthdate.get())
    msg+='\nAGE:  '+str(age.get())
    msg+='\nGENDER:  '+gender.get()
    msg+='\nBLOODGROUP:  '+bloodgroup.get()
    msg+='\nMOBILE NO.:  '+str(mobile.get())
    msg+='\nCOURSE:  '+course.get()
    msg+='\nADDRESS:  '+txtAddress.get(0.0,END).strip()
    msg+='\nCITY:  '+city.get()+'\n\n'

    txtResult.delete(0.0,END)
    txtResult.insert(0.0,msg)

    btnPDF.config(state="normal")
    btnAudio.config(state="normal")
    btnSave.config(state="normal")
    btnTranslate.config(state="normal")
    btnHTML.config(state="normal")
    btnQRCode.config(state="normal")

    btnQRCode.invoke()      
    messagebox.showinfo("ID CARD",msg)  
    
     
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
    city.set(value='BHOPAL')
    bloodgroup.set(value="B+")
    birthdate.set(value="01-01-2006")
    mobile.set(value="3054120505")
    course.set(value="BCA")
    
    txtAddress.delete(0.0,END)
    txtResult.delete(0.0,END)
    lblQRCode.config(image=img)

    btnHTML.config(state="disabled")
    btnPDF.config(state="disabled")
    btnAudio.config(state="disabled")
    btnSave.config(state="disabled")
    btnTranslate.config(state="disabled")
   
def pdfClick():
    filename=name.get()+"_"+str(age.get())
    htmlfile=filename+".html"
    if not os.path.exists(htmlfile):
        messagebox.showerror("file Not Found",f"Sorry {filename} File Not Found")
        return
    #Otherwise
    pdffile=filename+".pdf"
    HTML(htmlfile).write_pdf(pdffile)    #weasypdf library
    messagebox.showinfo("Saved",
    f'PDF saved at {os.getcwd()}/{filename}')


    
    
def translateClick():
    A=src_lang.get().lower()
    B=tgt_lang.get().lower()
    data=(txtResult.get("0.0",END))

    if not src_lang or not tgt_lang:
        messagebox.showwarning("ERROR","SELECT BOTH SOURCES,target")
        return

    if not data:
        messagebox.showwarning("Empty Input","SOURCE TEXT IS EMPTY")
        return
    try:
        translator=Translator()
        translated=translator.translate(data,src=A,dest=B)
        txtResult.insert(END,translated)
        
    except Exception as e:
        messagebox.showerror("Translation Error",f"An error occured:{e}")
        return  
  


def saveClick():
    confirm=askyesno(title="confirmation",message="Are you sure to SAVE it?")
    if not confirm:
        return
    #Otherwise,collect and save data
    name1=name.get( ).title()
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
    qrcode1=name.get()+str(age.get())+".png"

    data=[name1,age1,gender1,city1,address1,married1,photo1,qrcode1,mobile1,birthdate1,bloodgroup1,course1]

    record=",".join(data)+"\n"

    with open('record.csv','a')as file:
        file.write(record)
        messagebox.showinfo('Record Saved',f'Record{name1} saved successfully')
  

def audioClick():
    filename=f'{os.getcwd()}\\{name.get()}-{age.get()}.mp3'
    print("Audio Click",filename)
    say=txtResult.get(0.0,END)
    language="hi"
    accent="co.in"
    tts=gTTS(text=say,lang=language,tld=accent)
    tts.save(filename)
    if os.path.exists(filename):
        playsound.playsound(filename)
        os.remove(filename)


def htmlClick():
    nothing1="one"
    name1=name.get().title()
    age1=str(age.get())
    gender1=gender.get()
    city1=city.get()
    address1=txtAddress.get(0.0,END).strip()
    mobile1=str(mobile.get().strip())
    birthdate1=str(birthdate.get())
    bloodgroup1=bloodgroup.get()
    course1=course.get()
    married1="Married"if married.get() else"Single"

    data1=[nothing1,name1,age1,gender1,city1,address1,married1,mobile1,birthdate1,bloodgroup1,course1]
    data2=",".join(data1)
    
    A="english"
    B=tgt_lang.get().lower()
    data3=data2
    translator=Translator()
    translated=translator.translate(data3,src=A,dest=B)
    data4=translated
    data5=str(data4).split(",")
    
    name1=name1+f'({data5[3]})'
    age1=age1+f'({data5[4]})'
    gender1+=f'({data5[5]})'
    city1+=f'({data5[6]})'
    address1+=f'({data5[7]})'
    married1+=f'({data5[8]})'
    mobile1+=f'({data5[9]})'
    birthdate1+=f'({data5[10]})'
    bloodgroup1+=f'({data5[11]})'
    course1+=f'({data5[12]})'

    photo1=name.get()+course.get()+".png"
    qrcode1=name.get()+str(age.get())+".png"
    
    data=[name1,age1,gender1,city1,address1,married1,photo1,qrcode1,mobile1,birthdate1,bloodgroup1,course1]

    html=genrateHTML(*data)
    frame4.load_html(html)
    filename=name1+"_"+str(age1)+".html"
    with open(filename,"w",encoding="utf-8")as file:
        file.write(html)
    webbrowser.open(f"file://{os.path.abspath(filename)}")
    
    

"""###########################################################"""
##frame1
frame1=LabelFrame(innerframe,text="Enter Your Information")
frame1.pack(fill=X,expand=True, anchor="n",padx=4,pady=3)

#NAME label
lblName=Label(frame1,text="ENTER NAME:")
lblName.grid(row=0,column=0)

txtName=Entry(frame1,width=30,textvariable=name)
txtName.grid(row=0,column=1,columnspan=2)


#birthdate
Label(frame1,text="BIRTH DATE[DD-MM-YYYY]:").grid(row=1,column=0)
txtBirthDate=Entry(frame1,width=15,textvariable=birthdate)
txtBirthDate.grid(row=1,column=1,columnspan=2,pady=5)

#age spinbox
Label(frame1,text="ENTER AGE:").grid(row=2,column=0)
spiAge=Spinbox(frame1,textvariable=age,from_=1,to=100)
spiAge.grid(row=2,column=1,columnspan=2)


#gender radio button
Label(frame1,text="SELECT GENDER:").grid(row=3,column=0)
#for male
rdoMale=Radiobutton(frame1,value="Male",text="Male",variable=gender)
rdoMale.select()
rdoMale.grid(row=3,column=1)
#for female
rdoFemale=Radiobutton(frame1,value="Female",text="Female",variable=gender)
rdoFemale.deselect()
rdoFemale.grid(row=3,column=2)


#Course cmb
Label(frame1,text="SELECT COURSE:").grid(row=4,column=0)
courses=["BCA","B_COM","BBA","M_COM","MA"]
cmbCourse=ttk.Combobox(frame1,values=courses,textvariable=course)
cmbCourse.grid(row=4,column=1,columnspan=2)


#bloodgroup
Label(frame1, text='BLOOD GROUP:').grid(row=5, column=0)
groups=['A++', 'A-' ,'B+',"B-","O+","O-",'AB+',"AB-"]
cmbBloodgroup=ttk.Combobox(frame1,values=groups, textvariable=bloodgroup)
cmbBloodgroup.grid(row=5, column=1,columnspan=2,pady=5)


#city combobox
Label(frame1,text="SELECT CITY OF YOUR BIRTH:").grid(row=6,column=0)
cities=["BHOPAL","UJJAIN","INDORE"]
cmbCity=ttk.Combobox(frame1,value=cities,textvariable=city)
cmbCity.grid(row=6,column=1,columnspan=2)


#address  multiline text
Label(frame1,text="ENTER ADDRESS:").grid(row=7,column=0)
txtAddress=Text(frame1,width=40,height=2)
txtAddress.grid(row=7,column=1,columnspan=2,pady=5)


#checkbutton for married or not
Label(frame1,text="ARE YOU MARRIED?").grid(row=8,column=0)
chkMarried=Checkbutton(frame1,variable=married,offvalue=False,onvalue=True)
chkMarried.grid(row=8,column=1,sticky="w")
"""###########################################################"""



"""###########################################################"""
##frame2
frame2=LabelFrame(innerframe,text="Result Is")
frame2.pack(anchor="n",expand=True,fill=BOTH,padx=10,pady=3)

#RESULT TEXT BOX
txtResult=Text(frame2,width=67,height=13,state="normal")
txtResult.grid(row=1,column=1,columnspan=3,padx=10,pady=3)

#DISPLAYING QR CODE LABEL
lblQRCode=Label(frame2,image=img)
lblQRCode.grid(row=1,column=3,columnspan=2,padx=10,pady=3)
"""###########################################################"""




"""###########################################################"""
##frame3
frame3=Frame(innerframe)
frame3.pack(fill=BOTH)

#result button
btnResult=Button(frame3,text="SHOW RESULT",command=resultClick)
btnResult.grid(row=0,column=0,columnspan=2,padx=25,pady=10)

#QR Code button
btnQRCode=Button(frame3,text="GENRATE QR CODE",command=qrcodeClick)
btnQRCode.grid(row=0,column=2,columnspan=2,padx=25,pady=10)

#Clear button
btnClear=Button(frame3,text="CLEAR",command=clearClick)
btnClear.grid(row=0,column=4,padx=25,columnspan=2,pady=10)

#SAVE BUTTON
btnSave=Button(frame3,text="SAVE TO CSV",command=saveClick)
btnSave.grid(row=0,column=6,columnspan=2,padx=25,pady=10)

#HTML BUTTON
btnHTML=Button(frame3,text="GENRATE HTML",command=htmlClick)
btnHTML.grid(row=1,column=0,columnspan=2,padx=25,pady=10)

#PDF BUTTON
btnPDF=Button(frame3,text="GENRATE PDF",command=pdfClick)
btnPDF.grid(row=1,column=2,columnspan=2,padx=25,pady=10)

#Audio button
btnAudio=Button(frame3,text="GENRATE AUDIO",command=audioClick)
btnAudio.grid(row=1,column=4,columnspan=2,padx=25,pady=10)


"""###########################################################"""
#FrameA
frameA=Frame(innerframe)
frameA.pack(fill=BOTH)


#source language
source_lang_label=Label(frameA,text="Source Language:")
source_lang_label.grid(row=0,column=0,sticky="w")

source_lang_combo=ttk.Combobox(frameA,values=lang_names,textvariable=src_lang)
source_lang_combo.grid(row=1,column=0) 


#translate button
btnTranslate=Button(frameA,text="Language change",command=translateClick)
btnTranslate.grid(row=1,column=1)


#traget language
target_lang_label=Label(frameA,text="Target Language:")
target_lang_label.grid(row=0,column=2,sticky="w")

target_lang_combo=ttk.Combobox(frameA,values=lang_names,textvariable=tgt_lang)
target_lang_combo.grid(row=1,column=2)

"""###########################################################"""
btnQRCode.config(state="disabled")
btnHTML.config(state="disabled")
btnPDF.config(state="disabled")
btnAudio.config(state="disabled")
btnSave.config(state="disabled")
btnTranslate.config(state="disabled")


"""###########################################################"""
##frame 4
frame4=HtmlFrame(innerframe,horizontal_scrollbar="auto")
frame4.pack(anchor="n",expand=True,fill=BOTH,pady=10)
html="<b>IDENTITY CARD APP</b>"
frame4.load_html(html)
"""###########################################################"""

canvas.configure(yscrollcommand=v_scroll.set)
innerframe.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=innerframe,anchor="w")


win.mainloop()



