from tkinter import *
def getHost():
    
    def get(e=None):
        ipVar.set(ip.get())
        portVar.set(int(port.get()))
    root = Tk()
    
    root.resizable(height = None, width = None)
    
    ipVar = StringVar(root)
    portVar = IntVar(root)
    Label(root,text="Enter host details.").grid(row=0,column=0,columnspan=2)
    Label(root,text="IP: ").grid(row=1,column=0)
    Label(root,text="Port: ").grid(row=2,column=0)
    ip = Entry(root)
    ip.grid(row=1,column=1)
    port = Entry(root)
    port.grid(row=2,column=1)
    Button(root,text="Enter",command=get).grid(row=3,column=0,columnspan=2)
    root.bind("<Return>",get)
    root.lift()
    root.wait_variable(ipVar)
    ip = ipVar.get()
    port = portVar.get()
    root.destroy()
    return ip,port