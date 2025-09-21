from tkinter import*
from tkinter import filedialog,messagebox,ttk
from tkinter.scrolledtext import ScrolledText
from googletrans import Translator,LANGUAGES


def open_file():
    file_path=filedialog.askopenfilename(filetypes=[("Text File","*.txt")])
    if file_path:
        with open(file_path,'r',encoding='utf-8')as file:
            content=file.read()
            source_text.delete("1.0",END)
            source_text.insert(END,content)

def save_file():
    file_path=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text File","*.txt")]) 
    if file_path:
        with open(file_path,'w',encoding='utf-8')as file:
            content=target_text.get("1.0",END).strip()
            file.write(content)
        messagebox.showinfo("Success","File saved successfully!")

def translate_text():
    src_lang=source_lang_combo.get()
    tgt_lang=target_lang_combo.get()
    text_to_translate=source_text.get("1.0",END).strip()
    if not src_lang or not tgt_lang:
        messagebox.showwarning("ERROR","SELECT BOTH SOURCES,target")
        return

    if not text_to_translate:
        messagebox.showwarning("Empty Input","SOURCE TEXT IS EMPTY")
        return

    try:
        translator=Translator()
        translated=translator.translate(text_to_translate,src=src_lang,dest=tgt_lang)
        target_text.delete("1.0",END)
        target_text.insert(END,translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error",f"An error occured:{e}")
        
win=Tk()
win.title("Language Translator")
win.geometry("600x400")

source_lang_combo = ttk.Combobox(win, values=list(LANGUAGES.keys()))
source_lang_combo.set("en")  # default English
source_lang_combo.grid(row=0, column=0, padx=5, pady=5)

target_lang_combo = ttk.Combobox(win, values=list(LANGUAGES.keys()))
target_lang_combo.set("hi")  # default Hindi
target_lang_combo.grid(row=0, column=4, padx=5, pady=5)


source_text=ScrolledText(win,wrap=WORD,height=5,width=25)
source_text.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

target_text=ScrolledText(win,wrap=WORD,height=5,width=25)
target_text.grid(row=2,column=4,columnspan=2,padx=5,pady=5)



convertbtn=Button(win,text="Convert",command=translate_text)
convertbtn.grid(row=2,column=2,padx=5,pady=5)

menu=Menu(win)
win.config(menu=menu)

file_menu =Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="OPEN",command=open_file)
file_menu.add_command(label="SAVE AS",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="EXIT",command=win.quit)

win.mainloop()

    
