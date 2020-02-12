from tkinter import *
class Window(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.text = Text(self)
        self.entryBar = Frame(self)
        self.input = Entry(self.entryBar,width=80)
        self.button = Button(self.entryBar,text="⮐",command=self._addEvent)
        
        self.text.grid(row=0,column=0,)
        self.input.grid(row=0,column=0,sticky=EW)
        self.button.grid(row=0,column=1,sticky=W)
        self.entryBar.grid(row=1,column=0)
        self.textStack = []
        self._loopFunc = None
        
        self.bind("<Return>",self._addEvent)
        
    def _addEvent(self,event=None):
        text = self.input.get()
        if text != "":
            self.input.delete(0, END)
            self.textStack.insert(0,text)
    
    def getNextEvent(self):
        if len(self.textStack) > 0:
            return self.textStack.pop()
        else:
            return False
    
    def getEvents(self):
        out = list(self.textStack)
        self.textStack = []
        return out
    
    def _loop(self):
        self._loopFunc()
        self.after(10,self._loop)
    
    def runLoop(self,func):
        self._loopFunc = func
        self.after(10,self._loop)
        self.mainloop()
    
    def _print(self,text):
        self.text.insert(END,text)