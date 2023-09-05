from tkinter import*
import random
import string
from tkinter import messagebox


def gen_pass():
    length =entry2.get()
    if len(length) <= 0:
        pvar.set("")
        messagebox.showwarning("ERROR!","Please enter a valid number")

    length = int(length)

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    pvar.set(password)

def reset():
    pvar.set("")


root= Tk()
root.geometry("420x370")
root.title("Random Password Generator")

label1=Label(root,text=" ",bg="white")
label1.place(x=0,y=0,height=370,width=420)

label2=Label(root,text="Random Password Generator",font=("calibre",15),bg="orange")
label2.place(x=60,y=30)

label3=Label(root,text="User Name:-",font=("calibre"),bg="white")
label3.place(x=0,y=100)

label4=Label(root,text="Password Length:-",font=("calibre"),bg="white")
label4.place(x=0,y=150)

pvar = StringVar()

label5=Label(root,text="Generated Password:-",font=("calibre"),bg="white")
label5.place(x=0,y=305)


button1=Button(root,text="Generate Password",font=("calibre"),bg="cyan",command=gen_pass)
button1.place(x=165,y=200,width=200)
button2=Button(root,text="Reset",font=("calibre"),bg="light green",command=reset)
button2.place(x=165,y=250,width=100)



entry1=Entry(root,font=('italic',10, 'bold'),relief=GROOVE,bg="white")
entry1.place(x=165,y=105,height=30,width=250)

entry2=Entry(root,font=('italic',10, 'bold'),relief=GROOVE,bg="white")
entry2.place(x=165,y=155,height=30,width=250)

entry3=Entry(root,font=('italic',10, 'bold'),relief=GROOVE,bg="white",textvariable=pvar)
entry3.place(x=165,y=305,height=30,width=250)



root.mainloop()
