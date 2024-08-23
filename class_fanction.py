import tkinter as tk
from tkinter import ttk

class ClacGui():
    def __init__(self):
        self.ischar = False
        
        self.window = tk.Tk()
        self.str_manitor = tk.StringVar(value="22")
        self.manitor = tk.Label(
            master=self.window,
            textvariable=self.str_manitor
            )
        self.bot_1= tk.Button(
            master=self.window,
            text="1",
            width=6,
            height=3,
            command=self.clicked_on_1
        )
        self.bot_2= tk.Button(
            master=self.window,
            text="2",
            width=6,
            height=3,
            command=self.clicked_on_2
        )
        self.bot_3= tk.Button(
            master=self.window,
            text="3",
            width=6,
            height=3,
            command=self.clicked_on_3
        )
        self.bot_dot= tk.Button(
            master=self.window,
            text=".",
            width=6,
            height=3,
            command=self.clicked_on_dot
          
        )
        self.bot_4= tk.Button(
            master=self.window,
            text="4",
            width=6,
            height=3,
            command=self.clicked_on_4
        )
        self.bot_5= tk.Button(
            master=self.window,
            text="5",
            width=6,
            height=3,
              command=self.clicked_on_5
        )
        self.bot_6= tk.Button(
            master=self.window,
            text="6",
            width=6,
            height=3,
              command=self.clicked_on_6
        )
        self.bot_plus= tk.Button(
            master=self.window,
            text="+",
            width=6,
            height=3
        )
        self.bot_7= tk.Button(
            master=self.window,
            text="7",
            width=6,
            height=3,
              command=self.clicked_on_7
        )
        self.bot_8= tk.Button(
            master=self.window,
            text="8",
            width=6,
            height=3,
            command=self.clicked_on_8
        )
        self.bot_9= tk.Button(
            master=self.window,
            text="9",
            width=6,
            height=3,
            command=self.clicked_on_9
        )
        self.bot_minus= tk.Button(
            master=self.window,
            text="-",
            width=6,
            height=3
        )
        self.bot_cross= tk.Button(
            master=self.window,
            text="*",
            width=6,
            height=3
        )
        self.bot_0= tk.Button(
            master=self.window,
            text="0",
            width=6,
            height=3,
            command=self.clicked_on_0
            
        )
        self.bot_clear= tk.Button(
            master=self.window,
            text="C",
            width=6,
            height=3
        )
        self.bot_eq= tk.Button(
            master=self.window,
            text="=",
            width=6,
            height=3
        )
        self.manitor.grid(row=0,column=0,columnspan=10,padx=10,pady=(10,10))
        self.bot_1.grid(row=1,column=0)
        self.bot_2.grid(row=1,column=1)
        self.bot_3.grid(row=1,column=2)
        self.bot_plus.grid(row=1,column=3)
        self.bot_4.grid(row=2,column=0)
        self.bot_5.grid(row=2,column=1)
        self.bot_6.grid(row=2,column=2)
        self.bot_minus.grid(row=2,column=3)
        self.bot_7.grid(row=3,column=0)
        self.bot_8.grid(row=3,column=1)
        self.bot_9.grid(row=3,column=2)
        self.bot_cross.grid(row=3,column=3)
        self.bot_dot.grid(row=4,column=0)
        self.bot_0.grid(row=4,column=1)
        self.bot_clear.grid(row=4,column=2)
        self.bot_eq.grid(row=4,column=3)
        self.isdot = False


        self.window.mainloop()
    def clicked_on_1(self):
        self.ischar=False
        self.str_manitor.set(self.str_manitor.get()+"1")
    
    def clicked_on_2(self):
        self.ischar=False
        self.str_manitor.set(self.str_manitor.get()+"2")
    
    def clicked_on_3(self):
        self.ischar=False
        self.str_manitor.set(self.str_manitor.get()+"3")
    
    def clicked_on_4(self):
        self.ischar=False
        self.str_manitor.set(self.str_manitor.get()+"4")
    
    def clicked_on_5(self):
        self.ischar=False
        self.str_manitor.set(self.str_manitor.get()+"5")
    def clicked_on_6(self):
        self.ischar=False
        self.str_manitor.set(self.str_manitor.get()+"6")
    def clicked_on_7(self):
        self.ischar=False
        self.str_manitor.set(self.str_manitor.get()+"7")
    def clicked_on_8(self):
        self.ischar=False
        self.str_manitor.set(self.str_manitor.get()+"8")
    def clicked_on_9(self):
        self.ischar=False
        self.str_manitor.set(self.str_manitor.get()+"9")
    def clicked_on_0(self):
        self.ischar=False
        self.str_manitor.set(self.str_manitor.get()+"0")
    def clicked_on_dot(self):
        self.ischar=False
        if not self.isdot:
            self.str_manitor.set(self.str_manitor.get()+".")
            self.isdot=True
            return
    def clicked_on_clear(self):
        self.str_manitor.set("")
        


ClacGui()