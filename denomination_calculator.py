from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Counter")
root.configure(bg = 'light blue')
root.geometry('650x400')

upload = Image.open('cash1.jpeg')
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)
label1 = Label(root,
               text='Hey user welcome to the denomination counter',
               bg='light blue'
               )
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    msgBox = messagebox.showinfo('Alert, do you want to the denomination count')
    if msgBox == "ok":
        topWin()
        
button1 = Button(root,
                 text=" let's get started",
                 command=msg,
                 bg='brown',
                 fg='white')
button1.place(x=260, y=360)

def topWin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg='light gray')
    top.geometry('600x350+50+50')
    
    lable = Label(top, text='Enter the amount', bg='light gray')
    entry = Entry(top)
    lbl = Label(top, text='here are  number of notes for each denomination')
    
    l1 = Label(top, text='2000', bg= 'light gray')
    l2 = Label(top, text='500' , bg= 'light gray')
    l3 = Label(top, text='100' , bg= 'light gray')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    
    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error, please enter a valid number.")
            
    btn = Button(top, text='Calculate',command=calculator, bg='brown', fg='white')
            
            
        
