from tkinter import *

# This is a test for git

# This is another edit to check the git function

window = Tk()
window.title("Kilogram Conversion")

def from_kg():
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.delete("1.0", END)
    t1.insert(END,grams)
    t2.delete("1.0", END)
    t2.insert(END,pounds)
    t3.delete("1.0", END)
    t3.insert(END,ounces)
    
    

b1 = Button(window, text = "Convert", command=from_kg)
b1.grid(row=0,column=2)



e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

e2=Label(window,text="Enter kilograms:")
e2.grid(row=0,column=0)

e3=Label(window,text="Grams")
e3.grid(row=1,column=0)

e4=Label(window,text="Pounds")
e4.grid(row=1,column=1)

e5=Label(window,text="Ounces")
e5.grid(row=1,column=2)

t1 = Text(window,height=1,width=20)
t1.grid(row=2,column=0)

t2 = Text(window,height=1,width=20)
t2.grid(row=2,column=1)

t3 = Text(window,height=1,width=20)
t3.grid(row=2,column=2)




window.mainloop()
