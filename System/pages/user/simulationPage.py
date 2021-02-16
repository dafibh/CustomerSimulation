import tkinter as tk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threading import Thread

class SimPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#d9d9d9")

        self.btn_Back = tk.Button(self)
        self.btn_Back.place(relx=0.014, rely=0.9, height=38, width=53)
        self.btn_Back.configure(activebackground="#ececec")
        self.btn_Back.configure(activeforeground="#000000")
        self.btn_Back.configure(background="#d9d9d9")
        self.btn_Back.configure(disabledforeground="#a3a3a3")
        self.btn_Back.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.btn_Back.configure(foreground="#000000")
        self.btn_Back.configure(highlightbackground="#d9d9d9")
        self.btn_Back.configure(highlightcolor="black")
        self.btn_Back.configure(pady="0")
        self.btn_Back.configure(text='''Back''')

        self.Labelframe1 = tk.LabelFrame(self)
        self.Labelframe1.place(relx=0.014, rely=0.02, relheight=0.87
                , relwidth=0.356)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Log''')
        self.Labelframe1.configure(background="#c0c0c0")

        self.logListbox = tk.Listbox(self.Labelframe1)
        self.logListbox.place(relx=0.032, rely=0.069, relheight=0.5
                , relwidth=0.92, bordermode='ignore')
        self.logListbox.configure(background="white")
        self.logListbox.configure(disabledforeground="#a3a3a3")
        self.logListbox.configure(font="TkFixedFont")
        self.logListbox.configure(foreground="#000000")
        
        self.itemListbox = tk.Listbox(self.Labelframe1)
        self.itemListbox.place(relx=0.032, rely=0.58, relheight=0.4
                , relwidth=0.92, bordermode='ignore')
        self.itemListbox.configure(background="white")
        self.itemListbox.configure(disabledforeground="#a3a3a3")
        self.itemListbox.configure(font="TkFixedFont")
        self.itemListbox.configure(foreground="#000000")

        self.Labelframe2 = tk.LabelFrame(self)
        self.Labelframe2.place(relx=0.386, rely=0.12, relheight=0.77
                , relwidth=0.6)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Statistics''')
        self.Labelframe2.configure(background="#c0c0c0")

        self.Canvas1 = tk.Canvas(self.Labelframe2)
        self.Canvas1.place(relx=0.024, rely=0.081, relheight=0.888, relwidth=0.96
                , bordermode='ignore')
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.btn_PlayPause = tk.Button(self)
        self.btn_PlayPause.place(relx=0.486, rely=0.02, height=38, width=53)
        self.btn_PlayPause.configure(activebackground="#ececec")
        self.btn_PlayPause.configure(activeforeground="#000000")
        self.btn_PlayPause.configure(background="#d9d9d9")
        self.btn_PlayPause.configure(disabledforeground="#a3a3a3")
        self.btn_PlayPause.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.btn_PlayPause.configure(foreground="#000000")
        self.btn_PlayPause.configure(highlightbackground="#d9d9d9")
        self.btn_PlayPause.configure(highlightcolor="black")
        self.btn_PlayPause.configure(pady="0")
        self.btn_PlayPause.configure(text='''⏯️''')

        self.btn_Forward = tk.Button(self)
        self.btn_Forward.place(relx=0.586, rely=0.02, height=38, width=53)
        self.btn_Forward.configure(activebackground="#ececec")
        self.btn_Forward.configure(activeforeground="#000000")
        self.btn_Forward.configure(background="#d9d9d9")
        self.btn_Forward.configure(disabledforeground="#a3a3a3")
        self.btn_Forward.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.btn_Forward.configure(foreground="#000000")
        self.btn_Forward.configure(highlightbackground="#d9d9d9")
        self.btn_Forward.configure(highlightcolor="black")
        self.btn_Forward.configure(pady="0")
        self.btn_Forward.configure(text='''⏭️''')

        self.btn_Rewind = tk.Button(self)
        self.btn_Rewind.place(relx=0.386, rely=0.02, height=38, width=53)
        self.btn_Rewind.configure(activebackground="#ececec")
        self.btn_Rewind.configure(activeforeground="#000000")
        self.btn_Rewind.configure(background="#d9d9d9")
        self.btn_Rewind.configure(disabledforeground="#a3a3a3")
        self.btn_Rewind.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.btn_Rewind.configure(foreground="#000000")
        self.btn_Rewind.configure(highlightbackground="#d9d9d9")
        self.btn_Rewind.configure(highlightcolor="black")
        self.btn_Rewind.configure(pady="0")
        self.btn_Rewind.configure(text='''⏮️''')

        self.btn_Save = tk.Button(self)
        self.btn_Save.place(relx=0.9, rely=0.02, height=38, width=53)
        self.btn_Save.configure(activebackground="#ececec")
        self.btn_Save.configure(activeforeground="#000000")
        self.btn_Save.configure(background="#d9d9d9")
        self.btn_Save.configure(disabledforeground="#a3a3a3")
        self.btn_Save.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.btn_Save.configure(foreground="#000000")
        self.btn_Save.configure(highlightbackground="#d9d9d9")
        self.btn_Save.configure(highlightcolor="black")
        self.btn_Save.configure(pady="0")
        self.btn_Save.configure(text='''Save''')

        self.btn_Sales = tk.Button(self)
        self.btn_Sales.place(relx=0.386, rely=0.9, height=38, width=123)
        self.btn_Sales.configure(activebackground="#ececec")
        self.btn_Sales.configure(activeforeground="#000000")
        self.btn_Sales.configure(background="#d9d9d9")
        self.btn_Sales.configure(disabledforeground="#a3a3a3")
        self.btn_Sales.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.btn_Sales.configure(foreground="#000000")
        self.btn_Sales.configure(highlightbackground="#d9d9d9")
        self.btn_Sales.configure(highlightcolor="black")
        self.btn_Sales.configure(pady="0")
        self.btn_Sales.configure(text='''Sales per Day''')

        self.btn_Customer = tk.Button(self)
        self.btn_Customer.place(relx=0.6, rely=0.9, height=38, width=173)
        self.btn_Customer.configure(activebackground="#ececec")
        self.btn_Customer.configure(activeforeground="#000000")
        self.btn_Customer.configure(background="#d9d9d9")
        self.btn_Customer.configure(disabledforeground="#a3a3a3")
        self.btn_Customer.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.btn_Customer.configure(foreground="#000000")
        self.btn_Customer.configure(highlightbackground="#d9d9d9")
        self.btn_Customer.configure(highlightcolor="black")
        self.btn_Customer.configure(pady="0")
        self.btn_Customer.configure(text='''Customers per Day''')

        self.btn_Stat3 = tk.Button(self)
        self.btn_Stat3.place(relx=0.886, rely=0.9, height=38, width=63)
        self.btn_Stat3.configure(activebackground="#ececec")
        self.btn_Stat3.configure(activeforeground="#000000")
        self.btn_Stat3.configure(background="#d9d9d9")
        self.btn_Stat3.configure(disabledforeground="#a3a3a3")
        self.btn_Stat3.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.btn_Stat3.configure(foreground="#000000")
        self.btn_Stat3.configure(highlightbackground="#d9d9d9")
        self.btn_Stat3.configure(highlightcolor="black")
        self.btn_Stat3.configure(pady="0")
        self.btn_Stat3.configure(text='''Stat 3''')

        #commands
        self.btn_Back.configure(command=lambda:self.controller.simBack())
        self.btn_PlayPause.configure(command=lambda:self.controller.playtoggle())
        self.btn_Sales.configure(command=lambda:self.stat1())
        self.btn_Customer.configure(command=lambda:self.stat2())
        self.btn_Forward.configure(command=lambda:self.controller.simulator.forward())
        self.btn_Rewind.configure(command=lambda:self.controller.simulator.backward())
        self.logListbox.bind('<Double-1>', lambda x: self.logClick())
      

    def logClick(self):
        string = self.logListbox.get(self.logListbox.curselection())
        a = string.split(' ')
        self.clearInventory()

        #change log to include transaction id
        """for i in self.tlist:
            if i.custid == a[2]:
                for j in i.items:
                    self.addInventory(str(j))"""


    def graphclick(self, event): #enlarging supposedly
        #fig = self.fig

        plt.show()

    def addItem(self, item):
        self.logListbox.insert(0,item)

    def addInventory(self, item):
        self.itemListbox.insert(tk.END,item)

    def clearInventory(self):
        self.itemListbox.delete(0,tk.END)

    def clearLog(self):
        self.clearInventory()
        self.logListbox.delete(0,tk.END)

    def setTransactionObjects(self, transactions):
        self.tlist = transactions

        print("SETTRANSACTION IN SIMPAGE")

        for i in self.tlist:
            dateonly = i.arrival.split(' ')
            print(i)
            print(dateonly[0])

        #for customer per day
        daycounter = 0
        self.dates = []
        self.dateslbl = []
        for i in self.tlist: #try to find how many different dates are there and put in list
            if daycounter == 0:
                dateonly = i.arrival.split(' ')
                d2 = dateonly[0].split('/')
                self.dateslbl.append(f"{d2[0]}/{d2[1]}")
                self.dates.append(dateonly[0])
                daycounter = daycounter + 1
            else:
                dateonly = i.arrival.split(' ')
                if dateonly[0] != self.dates[len(self.dates)-1]:
                    d2 = dateonly[0].split('/')
                    self.dateslbl.append(f"{d2[0]}/{d2[1]}")
                    self.dates.append(dateonly[0])
                    daycounter = daycounter + 1

        print("-----------------------DATES-------------------")
        print(f"number of dates {daycounter}")
        print("dates")
        for i in self.dates:
            print(i)

        #try to find how many customer per day
        self.customerAmounts = [] 
        for i in range(daycounter):
            self.customerAmounts.append(0)

        for i in self.tlist:
            for j in range(daycounter):
                dateonly = i.arrival.split(' ')
                if dateonly[0] == self.dates[j]:
                    self.customerAmounts[j] = self.customerAmounts[j] + 1
                    break
        
        #try to find sales per day

        self.sales = []
        for i in range(daycounter):
            self.sales.append(0)

        for i in self.tlist:
            for j in range(daycounter):
                dateonly = i.arrival.split(' ')
                if dateonly[0] == self.dates[j]:
                    for x in i.items:
                        self.sales[j] = self.sales[j] + float(x['price'])
                    break



        print("Customer AMounts")
        for i in range(daycounter):
            print(f"{self.dates[i]} - {self.customerAmounts[i]}")
        #get from t and l the labels of x and y lists
        #put in self variable


    def myplotcode(self,lx,ly, xlabel, ylabel):
        

        x=np.array(lx)
        y=np.array(ly)

        plt.close(1)
        fig,ax=plt.subplots()
        ax.plot(x,y,marker='.',color='r',linestyle='-')
        ax.set_ylabel(ylabel)
        ax.set_xlabel(xlabel)

        return fig

    """def myplotcode2(self):
        x = np.linspace(0,2*np.pi)
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(x, x**2)
        
        return fig"""

    def stat1(self):
        try: 
            self.Canvas1.get_tk_widget().pack_forget()
        except AttributeError: 
            pass
        self.fig = self.myplotcode(self.dateslbl,self.sales,"Dates","Sales (RM)")
        self.Canvas1 = FigureCanvasTkAgg(self.fig, master=self.Labelframe2)
        self.Canvas1.get_tk_widget().pack()
        self.Canvas1.callbacks.connect('button_press_event', self.graphclick)

    def stat2(self):
        try: 
            self.Canvas1.get_tk_widget().pack_forget()
        except AttributeError: 
            pass 
        self.fig = self.myplotcode(self.dateslbl, self.customerAmounts, "Dates", "Customer")
        self.Canvas1 = FigureCanvasTkAgg(self.fig, master=self.Labelframe2)
        self.Canvas1.get_tk_widget().pack()
        self.Canvas1.callbacks.connect('button_press_event', self.graphclick)









