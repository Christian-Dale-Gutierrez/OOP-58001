from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry("500x250+10+20")
window.title("Midterm in OOP")

str1 = StringVar()
str2 = StringVar()

def fullname():
    prnt = (str1.get())
    str2.set(prnt)

label = Label(window, text = "Enter your fullname:", fg = "red")
label.place(x=70, y=70)

txtfld1 = Entry(window, bd = 5)
txtfld1.place(x=270, y=65)

button = Button(window, text = "Click to display your Fullname", fg = "red", command=lambda:fullname())
button.place (x=60, y=140)

txtfld2 = Entry(window, bd = 5, textvariable=str2)
txtfld2.place(x=270, y=140)

window.mainloop()