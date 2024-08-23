import tkinter as tk
from tkinter import ttk

class ClacGui():
    def __init__(self):
        self.ischar = False
        self.isdot = False
        self.isplus = False
        self.isminus = False
        self.iscross = False
        self.iseq = False
       
        self.window = tk.Tk()
        self.window.bind("<KeyPress-1>",self.clicked_on_1)
        self.window.bind("<KeyPress-2>",self.clicked_on_2)
        self.window.bind("<KeyPress-3>",self.clicked_on_3)
        self.window.bind("<KeyPress-4>",self.clicked_on_4)
        self.window.bind("<KeyPress-5>",self.clicked_on_5)
        self.window.bind("<KeyPress-6>",self.clicked_on_6)
        self.window.bind("<KeyPress-7>",self.clicked_on_7)
        self.window.bind("<KeyPress-8>",self.clicked_on_8)
        self.window.bind("<KeyPress-9>",self.clicked_on_9)
        self.window.bind("<KeyPress-0>",self.clicked_on_0)
        self.window.bind("<KeyPress-+>",self.clicked_on_plus)
        self.window.bind("<KeyPress-->",self.clicked_on_minus)
        self.window.bind("<KeyPress-*>",self.clicked_on_cross)
        self.window.bind("<Return>",self.clicked_on_eq)
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
            height=3,
            command=self.clicked_on_plus
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
            height=3,
            command= self.clicked_on_minus
        )
        self.bot_cross= tk.Button(
            master=self.window,
            text="*",
            width=6,
            height=3,
            command=self.clicked_on_cross
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
            height=3,
            command=self.clicked_on_clear
        )
        self.bot_eq= tk.Button(
            master=self.window,
            text="=",
            width=6,
            height=3,
            command=self.clicked_on_eq
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

        
        self.window.mainloop()
    def clicked_on_1(self,*args):
        self.make_missons_false()
        self.str_manitor.set(self.str_manitor.get()+"1")
    
    def clicked_on_2(self,*args):
        self.make_missons_false()
        self.str_manitor.set(self.str_manitor.get()+"2")
    
    def clicked_on_3(self,*args):
        self.make_missons_false()
        self.str_manitor.set(self.str_manitor.get()+"3")
    
    def clicked_on_4(self,*args):
        self.make_missons_false()
        self.str_manitor.set(self.str_manitor.get()+"4")
    
    def clicked_on_5(self,*args):
        self.make_missons_false()
        self.str_manitor.set(self.str_manitor.get()+"5")
    def clicked_on_6(self,*args):
        self.make_missons_false()
        self.str_manitor.set(self.str_manitor.get()+"6")
    def clicked_on_7(self,*args):
        self.make_missons_false()
        self.str_manitor.set(self.str_manitor.get()+"7")
    def clicked_on_8(self,*args):
        self.make_missons_false()
        self.str_manitor.set(self.str_manitor.get()+"8")
    def clicked_on_9(self,*args):
        self.make_missons_false()
        self.str_manitor.set(self.str_manitor.get()+"9")
    def clicked_on_0(self,*args):
        self.make_missons_false()
        if len(self.str_manitor.get())!=0:
            self.str_manitor.set(self.str_manitor.get()+"0")
    def clicked_on_dot(self,*args):
        self.ischar = self.isplus=self.cross = self.eq = self.iscross = True
        if not self.isdot and self.str_manitor.get()!="":
            self.str_manitor.set(self.str_manitor.get()+".")
            self.isdot=True
            return
    def make_missons_false(self):
        self.isdot=False
        self.ischar=False
        self.isplus=False
        self.iscross=False
        self.iseq=False
        self.isminus = False

    def clicked_on_clear(self,*args):
        self.str_manitor.set("")
        self.make_missons_false()
        
    def clicked_on_plus(self,*args):
        if self.ischar ==False and self.isplus==False:
            self.isplus=True
            self.ischar = True
            self.str_manitor.set(self.str_manitor.get()+"+")  
        elif (self.ischar==True and self.isplus==False):
            self.make_missons_false()
            self.ischar= True
            self.isplus = True
            new_str =self.str_manitor.get()
            new_str = new_str[:-1]
            self.str_manitor.set(new_str+"+")
        return
    
    def clicked_on_minus(self,*args):
        if self.ischar ==False and self.isminus==False:
            self.isminus=True
            self.ischar = True
            self.str_manitor.set(self.str_manitor.get()+"-")  
        elif (self.ischar==True and self.isminus==False):
            self.make_missons_false()
            self.ischar= True
            self.isminus = True
            new_str =self.str_manitor.get()
            new_str = new_str[:-1]
            self.str_manitor.set(new_str+"-")
        return
    def clicked_on_cross(self,*args):
        if self.ischar ==False and self.iscross==False:
            self.iscross=True
            self.ischar = True
            self.str_manitor.set(self.str_manitor.get()+"*")  
        elif (self.ischar==True and self.iscross==False):
            self.make_missons_false()
            self.ischar= True
            self.iscross = True
            new_str =self.str_manitor.get()
            new_str = new_str[:-1]
            self.str_manitor.set(new_str+"*")
        return
    
    def clicked_on_eq(self,*args):
        self.make_missons_false()
        res=0
        lastchar = [-1,"+"]
        missons_txt = self.str_manitor.get()
        for index,char in enumerate(missons_txt):
            print(index,char)
            if index==0 and char == "-":
                lastchar[1]= "-"
            if  char not in "0123456789." and index!=0:
                res = self.count_by_char(res,float(missons_txt[lastchar[0]+1:index]),lastchar[1])
                lastchar = [index,char]
                print(lastchar)
            elif index == len(missons_txt)-1:
                print(missons_txt[lastchar[0]:index] , "end")
                res = self.count_by_char(res,float(missons_txt[lastchar[0]+1:index+1]),lastchar[1])
            self.str_manitor.set(res)

    def count_by_char(self,num1,num2,digit):
        if digit =="+":
            return num1+num2
        elif digit == "-":
            return num1-num2
        elif digit == "*":
            return num1*num2
        else:
            print(digit)
            raise Exception("{} is invalid digit".format(digit))

ClacGui()