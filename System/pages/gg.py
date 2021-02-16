import tkinter as tk

class GG(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.429, rely=0.04, height=21, width=94)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Transaction File''')

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.029, rely=0.1, height=21, width=35)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''File :''')

        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.1, rely=0.1, height=20, relwidth=0.749)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.871, rely=0.1, height=24, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Select File''')

        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.043, rely=0.2, height=21, width=643)
        self.Label3.configure(background="#c3c3c3")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Label''')

        self.Label4 = tk.Label(self)
        self.Label4.place(relx=0.043, rely=0.26, height=21, width=164)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Transaction Line ID Column :''')

        self.text_CustomerID = tk.Entry(self)
        self.text_CustomerID.place(relx=0.771, rely=0.26, height=20
                , relwidth=0.049)
        self.text_CustomerID.configure(background="white")
        self.text_CustomerID.configure(disabledforeground="#a3a3a3")
        self.text_CustomerID.configure(font="TkFixedFont")
        self.text_CustomerID.configure(foreground="#000000")
        self.text_CustomerID.configure(highlightbackground="#d9d9d9")
        self.text_CustomerID.configure(highlightcolor="black")
        self.text_CustomerID.configure(insertbackground="black")
        self.text_CustomerID.configure(selectbackground="blue")
        self.text_CustomerID.configure(selectforeground="white")

        self.Label5 = tk.Label(self)
        self.Label5.place(relx=0.343, rely=0.26, height=21, width=117)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Datetime Column :''')

        self.text_Datetime = tk.Entry(self)
        self.text_Datetime.place(relx=0.514, rely=0.26, height=20
                , relwidth=0.049)
        self.text_Datetime.configure(background="white")
        self.text_Datetime.configure(disabledforeground="#a3a3a3")
        self.text_Datetime.configure(font="TkFixedFont")
        self.text_Datetime.configure(foreground="#000000")
        self.text_Datetime.configure(highlightbackground="#d9d9d9")
        self.text_Datetime.configure(highlightcolor="black")
        self.text_Datetime.configure(insertbackground="black")
        self.text_Datetime.configure(selectbackground="blue")
        self.text_Datetime.configure(selectforeground="white")

        self.text_TransID = tk.Entry(self)
        self.text_TransID.place(relx=0.286, rely=0.26, height=20, relwidth=0.049)

        self.text_TransID.configure(background="white")
        self.text_TransID.configure(disabledforeground="#a3a3a3")
        self.text_TransID.configure(font="TkFixedFont")
        self.text_TransID.configure(foreground="#000000")
        self.text_TransID.configure(highlightbackground="#d9d9d9")
        self.text_TransID.configure(highlightcolor="black")
        self.text_TransID.configure(insertbackground="black")
        self.text_TransID.configure(selectbackground="blue")
        self.text_TransID.configure(selectforeground="white")

        self.Label6 = tk.Label(self)
        self.Label6.place(relx=0.571, rely=0.26, height=21, width=133)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Customer ID Column :''')






