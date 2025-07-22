import tkinter as tk
import os 
from tkinter.filedialog import askopenfile,asksaveasfile
from tkinter.messagebox import showinfo
from tkinter import simpledialog
from tkinter import font

root=tk.Tk()
def open_file():
        global file
        file=askopenfile(defaultextension=".txt",
                filetypes=[("All files","*.*"),("text Documents","*.txt")])
        
        if file=="":
         file=None
        else:
         root.title(os.path.basename(file)+"-Notepad")
         text_Area.delete("1.0", tk.END)
         f=open(file,"r")
         text_Area.insert("1.0",f.read())
         f.close
def new_file():
        global file
        root.title("Untitled - Notepad")
        text_Area.delete("1.0", tk.END)
        
def save():
        global file
        if file==None:
                file=asksaveasfile(initialfile="untitle.txt",defaultextension=".txt"
                                   ,filetypes=[("All files","*.*"),("Text Documents","*.txt")])
 
 
 
def copy():
        text_Area.event_generate(("<<Copy>>"))
def cut():
        text_Area.event_generate(("<<Cut>>"))
def paste():
        text_Area.event_generate(("<<Paste>>"))
 
 
def help():
        showinfo("Notepad","Devolped BY HARIS NADEEM ")    
def new_font():
        size=simpledialog.askinteger("NotePad","Enter font size (e.g. 10, 12, 18):")
        if size:
                new_font = font.Font(family="Arial", size=size)
                text_Area.config(font=new_font)
        
                       
root.geometry("300x250")
root.title("NOTEPAD")
# for text:
text_Area = tk.Text(root, font=("Arial", 12))
file=None
text_Area.pack(expand=True, fill='both')
# text_Area=tk.Text(root)
# text_Area.pack(expand=True,fill="both")
# for logo:
root.iconphoto(False, tk.PhotoImage(file="logo.png"))
# for file :
toolbar=tk.Menu(root)
m1=tk.Menu(toolbar,tearoff=0)
m1.add_command(label="open",command=open_file)
m1.add_command(label="New File",command=new_file)

m1.add_separator()
m1.add_command(label="Save",command=save)

m1.add_command(label="Exit",command=quit)
toolbar.add_cascade(label="File",menu=m1)
# for Edit :
m2=tk.Menu(toolbar,tearoff=0)
m2.add_command(label="copy",command=copy)
m2.add_command(label="cut",command=cut)
m2.add_command(label="paste",command=paste)
m2.add_command(label="Font",command=new_font)

toolbar.add_cascade(label="Edit",menu=m2)
# for Help :
m3=tk.Menu(toolbar,tearoff=0)
m3.add_command(label="About",command=help)

toolbar.add_cascade(label="View",menu=m3)

root.config(menu=toolbar)




root.mainloop()