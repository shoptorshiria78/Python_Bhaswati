from tkinter import *


root = Tk()
root.geometry('400x300')
root.title("main")

def topWin():
    top = Toplevel()
    top.geometry('180x100')
    top.title("top level")
    
    lable = Label(top, text=" top level window")
    lable.pack()
    
    top.mainloop()
    
lable2 = Label(root, text="root window")
button = Button(root, text="click here to open another window", command=topWin)

lable2.pack()
button.pack()

root.mainloop()