import tkinter as tk



class Test(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        top = tk.Frame(self)
        

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.386, rely=0.02, height=24, width=130)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Transaction File''')

        self.Label1.pack()

        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.086, rely=0.28, height=20, relwidth=0.12)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.043, rely=0.28, height=21, width=34)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''ID''')






