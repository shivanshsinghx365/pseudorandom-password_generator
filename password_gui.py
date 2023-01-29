from tkinter import *
from random import randint

#made a window
root = Tk()
root.title("Secure Password Generator")
root.geometry("420x278")

#added labels & entry box
lf=LabelFrame(root, text="How many characters")
lf.pack(pady=25)

entry=Entry(lf,font=("Ubuntu Mono",24))
entry.pack(padx=25,pady=25)


password=Entry(root,text='',font=("Ubuntu Mono",24),bd=0,bg='#d9d9d9')
password.pack(padx=25)

#created functions to automatically copy and generate password
def newrandom(): 
    password.delete(0,END)
    length=int(entry.get())
    pwd=''
    for i in range(length):
        k=randint(33,126)
        pwd+=chr(k)
    password.insert(0,pwd)

def clipboard():
    root.clipboard_clear()
    root.clipboard_append(password.get())

frame=Frame(root)
frame.pack(pady=25)

#created a generate button that uses both automatically copy and generate password functions
generator=Button(frame,text="Generate Strong Password",command=lambda:[newrandom(),clipboard()])
generator.pack(padx=10)

root.mainloop()
