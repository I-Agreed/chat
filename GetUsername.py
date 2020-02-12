from tkinter import *
def getHost():
    
    def get(e=None):
        userVar.set(ip.get())
    root = Tk()
    
    root.resizable(height = None, width = None)
    
    userVar = StringVar(root)
    portVar = IntVar(root)
    Label(root,text="Enter username.").grid(row=0,column=0,columnspan=2)
    Label(root,text="Username: ").grid(row=1,column=0)
    user = Entry(root)
    user.grid(row=1,column=1)
    Button(root,text="Enter",command=get).grid(row=3,column=0,columnspan=2)
    root.bind("<Return>",get)
    root.lift()
    root.wait_variable(userVar)
    user = userVar.get()
    root.destroy()
    return user