from tkinter import *

window = Tk()
window.title("Tkinter Sample Window")
window.geometry("300x300")

greeting = Label(text="Hello user", fg="black", bg="white")
button = Button(text="Click Me", bg="black", fg="white")
entry = Entry(fg="yellow", bg="blue", width=50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
lable = Label(master=frame, text='Sample Frame')
lable.pack()

textBox = Text(fg="green", bg="yellow")
textBox.pack()

window.mainloop()