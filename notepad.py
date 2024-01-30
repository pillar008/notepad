from tkinter import *


root  = Tk()

root.geometry("800x200")
root.minsize(400,200)
root.title("Neeraj")

def hello():
    print("This is a hello button")

# f1 = Frame(root, bg="green", borderwidth=6, relief=SUNKEN)
# f1.pack(side=LEFT, fill="y",pady=35)

# f2 = Frame(root, borderwidth=6, relief=SUNKEN)
# f2.pack(side=TOP, fill="x")

# l1=Label(f2,text="Welcome")
# l1.pack()

# l1=Label(f1,text="Notepad")
# l1.pack(pady=142)

# b1= Button(f2, fg="red",text="Print Now", command=hello)
# b1.pack()

# var = Label(text="Hello this is my first gui app")
# var.pack()
    

# ----------------------------------------------------------------
    
def getvalue():
    print(f"The value of user is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")

user= Label(root,text="Username:")
password = Label(root, text="Password:")
user.grid(row=0, column=0)
password.grid(row=1, column=0)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable= uservalue)
passentry = Entry(root, textvariable= passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvalue).grid()
# ----------------------------------------------------------------

root.mainloop()
