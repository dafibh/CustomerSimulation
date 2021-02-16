import tkinter as tk

class Admin_Import(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self)
        self.Label1.place(x=260, y=11, height=35, width=175)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 16 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Import Records''')

        self.Labelframe1 = tk.LabelFrame(self)
        self.Labelframe1.place(x=10, y=50, height=165, width=679)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font="-family {Segoe UI} -size 13 -weight bold -slant italic")
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Transaction File''')
        self.Labelframe1.configure(background="#d9d9d9")

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(x=10, y=30, height=21, width=34, bordermode='ignore')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''File :''')

        self.lbl_TFile = tk.Label(self.Labelframe1)
        self.lbl_TFile.place(x=50, y=30, height=21, width=534
                , bordermode='ignore')
        self.lbl_TFile.configure(background="#b1b1b1")
        self.lbl_TFile.configure(disabledforeground="#a3a3a3")
        self.lbl_TFile.configure(foreground="#000000")
        self.lbl_TFile.configure(text='''File Location''')

        self.btn_TChoose = tk.Button(self.Labelframe1)
        self.btn_TChoose.place(x=590, y=30, height=24, width=77
                , bordermode='ignore')
        self.btn_TChoose.configure(activebackground="#ececec")
        self.btn_TChoose.configure(activeforeground="#000000")
        self.btn_TChoose.configure(background="#d9d9d9")
        self.btn_TChoose.configure(disabledforeground="#a3a3a3")
        self.btn_TChoose.configure(foreground="#000000")
        self.btn_TChoose.configure(highlightbackground="#d9d9d9")
        self.btn_TChoose.configure(highlightcolor="black")
        self.btn_TChoose.configure(pady="0")
        self.btn_TChoose.configure(text='''Choose File''')

        self.lbl_TFirst = tk.Label(self.Labelframe1)
        self.lbl_TFirst.place(x=10, y=90, height=30, width=653
                , bordermode='ignore')
        self.lbl_TFirst.configure(activebackground="#f9f9f9")
        self.lbl_TFirst.configure(activeforeground="black")
        self.lbl_TFirst.configure(background="#b1b1b1")
        self.lbl_TFirst.configure(disabledforeground="#a3a3a3")
        self.lbl_TFirst.configure(foreground="#000000")
        self.lbl_TFirst.configure(highlightbackground="#d9d9d9")
        self.lbl_TFirst.configure(highlightcolor="black")
        self.lbl_TFirst.configure(text='''First Line''')

        self.Label4 = tk.Label(self.Labelframe1)
        self.Label4.place(x=290, y=60, height=21, width=94, bordermode='ignore')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 9 -slant italic")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Column Setting''')

        self.Label5 = tk.Label(self.Labelframe1)
        self.Label5.place(x=10, y=130, height=21, width=134, bordermode='ignore')

        self.Label5.configure(anchor='e')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Transaction ID Column :''')

        self.tf_TransactionID1 = tk.Entry(self.Labelframe1)
        self.tf_TransactionID1.place(x=150, y=130, height=20, width=34
                , bordermode='ignore')
        self.tf_TransactionID1.configure(background="white")
        self.tf_TransactionID1.configure(disabledforeground="#a3a3a3")
        self.tf_TransactionID1.configure(font="TkFixedFont")
        self.tf_TransactionID1.configure(foreground="#000000")
        self.tf_TransactionID1.configure(insertbackground="black")

        self.Label5_1 = tk.Label(self.Labelframe1)
        self.Label5_1.place(x=200, y=130, height=21, width=104
                , bordermode='ignore')
        self.Label5_1.configure(activebackground="#f9f9f9")
        self.Label5_1.configure(activeforeground="black")
        self.Label5_1.configure(anchor='e')
        self.Label5_1.configure(background="#d9d9d9")
        self.Label5_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1.configure(foreground="#000000")
        self.Label5_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1.configure(highlightcolor="black")
        self.Label5_1.configure(text='''Datetime Column :''')

        self.tf_Datetime = tk.Entry(self.Labelframe1)
        self.tf_Datetime.place(x=310, y=130, height=20, width=34
                , bordermode='ignore')
        self.tf_Datetime.configure(background="white")
        self.tf_Datetime.configure(disabledforeground="#a3a3a3")
        self.tf_Datetime.configure(font="TkFixedFont")
        self.tf_Datetime.configure(foreground="#000000")
        self.tf_Datetime.configure(highlightbackground="#d9d9d9")
        self.tf_Datetime.configure(highlightcolor="black")
        self.tf_Datetime.configure(insertbackground="black")
        self.tf_Datetime.configure(selectbackground="blue")
        self.tf_Datetime.configure(selectforeground="white")

        self.Label5_1_1 = tk.Label(self.Labelframe1)
        self.Label5_1_1.place(x=360, y=130, height=21, width=124
                , bordermode='ignore')
        self.Label5_1_1.configure(activebackground="#f9f9f9")
        self.Label5_1_1.configure(activeforeground="black")
        self.Label5_1_1.configure(anchor='e')
        self.Label5_1_1.configure(background="#d9d9d9")
        self.Label5_1_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1_1.configure(foreground="#000000")
        self.Label5_1_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1_1.configure(highlightcolor="black")
        self.Label5_1_1.configure(text='''Customer ID Column :''')

        self.tf_CustomerID = tk.Entry(self.Labelframe1)
        self.tf_CustomerID.place(x=490, y=130, height=20, width=34
                , bordermode='ignore')
        self.tf_CustomerID.configure(background="white")
        self.tf_CustomerID.configure(disabledforeground="#a3a3a3")
        self.tf_CustomerID.configure(font="TkFixedFont")
        self.tf_CustomerID.configure(foreground="#000000")
        self.tf_CustomerID.configure(highlightbackground="#d9d9d9")
        self.tf_CustomerID.configure(highlightcolor="black")
        self.tf_CustomerID.configure(insertbackground="black")
        self.tf_CustomerID.configure(selectbackground="blue")
        self.tf_CustomerID.configure(selectforeground="white")

        self.Label5_1_1 = tk.Label(self.Labelframe1)
        self.Label5_1_1.place(x=550, y=130, height=21, width=74
                , bordermode='ignore')
        self.Label5_1_1.configure(activebackground="#f9f9f9")
        self.Label5_1_1.configure(activeforeground="black")
        self.Label5_1_1.configure(anchor='e')
        self.Label5_1_1.configure(background="#d9d9d9")
        self.Label5_1_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1_1.configure(foreground="#000000")
        self.Label5_1_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1_1.configure(highlightcolor="black")
        self.Label5_1_1.configure(text='''Start Row :''')

        self.tf_TstartRow = tk.Entry(self.Labelframe1)
        self.tf_TstartRow.place(x=630, y=130, height=20, width=34
                , bordermode='ignore')
        self.tf_TstartRow.configure(background="white")
        self.tf_TstartRow.configure(disabledforeground="#a3a3a3")
        self.tf_TstartRow.configure(font="TkFixedFont")
        self.tf_TstartRow.configure(foreground="#000000")
        self.tf_TstartRow.configure(highlightbackground="#d9d9d9")
        self.tf_TstartRow.configure(highlightcolor="black")
        self.tf_TstartRow.configure(insertbackground="black")
        self.tf_TstartRow.configure(selectbackground="blue")
        self.tf_TstartRow.configure(selectforeground="white")

        self.Labelframe1_1 = tk.LabelFrame(self)
        self.Labelframe1_1.place(x=10, y=240, height=205, width=679)
        self.Labelframe1_1.configure(relief='groove')
        self.Labelframe1_1.configure(font="-family {Segoe UI} -size 13 -weight bold -slant italic")
        self.Labelframe1_1.configure(foreground="black")
        self.Labelframe1_1.configure(text='''Transaction Line File''')
        self.Labelframe1_1.configure(background="#d9d9d9")
        self.Labelframe1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_1.configure(highlightcolor="black")

        self.Label2_1 = tk.Label(self.Labelframe1_1)
        self.Label2_1.place(x=10, y=30, height=21, width=34, bordermode='ignore')

        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''File :''')

        self.lbl_TLineFile = tk.Label(self.Labelframe1_1)
        self.lbl_TLineFile.place(x=50, y=30, height=21, width=534
                , bordermode='ignore')
        self.lbl_TLineFile.configure(activebackground="#f9f9f9")
        self.lbl_TLineFile.configure(activeforeground="black")
        self.lbl_TLineFile.configure(background="#b1b1b1")
        self.lbl_TLineFile.configure(disabledforeground="#a3a3a3")
        self.lbl_TLineFile.configure(foreground="#000000")
        self.lbl_TLineFile.configure(highlightbackground="#d9d9d9")
        self.lbl_TLineFile.configure(highlightcolor="black")
        self.lbl_TLineFile.configure(text='''File Location''')

        self.btn_TLineChoose = tk.Button(self.Labelframe1_1)
        self.btn_TLineChoose.place(x=590, y=30, height=24, width=77
                , bordermode='ignore')
        self.btn_TLineChoose.configure(activebackground="#ececec")
        self.btn_TLineChoose.configure(activeforeground="#000000")
        self.btn_TLineChoose.configure(background="#d9d9d9")
        self.btn_TLineChoose.configure(disabledforeground="#a3a3a3")
        self.btn_TLineChoose.configure(foreground="#000000")
        self.btn_TLineChoose.configure(highlightbackground="#d9d9d9")
        self.btn_TLineChoose.configure(highlightcolor="black")
        self.btn_TLineChoose.configure(pady="0")
        self.btn_TLineChoose.configure(text='''Choose File''')

        self.lbl_TLineFirst = tk.Label(self.Labelframe1_1)
        self.lbl_TLineFirst.place(x=10, y=90, height=30, width=653
                , bordermode='ignore')
        self.lbl_TLineFirst.configure(activebackground="#f9f9f9")
        self.lbl_TLineFirst.configure(activeforeground="black")
        self.lbl_TLineFirst.configure(background="#b1b1b1")
        self.lbl_TLineFirst.configure(disabledforeground="#a3a3a3")
        self.lbl_TLineFirst.configure(foreground="#000000")
        self.lbl_TLineFirst.configure(highlightbackground="#d9d9d9")
        self.lbl_TLineFirst.configure(highlightcolor="black")
        self.lbl_TLineFirst.configure(text='''First Line''')

        self.Label4_1 = tk.Label(self.Labelframe1_1)
        self.Label4_1.place(x=290, y=60, height=21, width=94
                , bordermode='ignore')
        self.Label4_1.configure(activebackground="#f9f9f9")
        self.Label4_1.configure(activeforeground="black")
        self.Label4_1.configure(background="#d9d9d9")
        self.Label4_1.configure(disabledforeground="#a3a3a3")
        self.Label4_1.configure(font="-family {Segoe UI} -size 9 -slant italic")
        self.Label4_1.configure(foreground="#000000")
        self.Label4_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1.configure(highlightcolor="black")
        self.Label4_1.configure(text='''Column Setting''')

        self.Label5_2 = tk.Label(self.Labelframe1_1)
        self.Label5_2.place(x=10, y=130, height=21, width=134
                , bordermode='ignore')
        self.Label5_2.configure(activebackground="#f9f9f9")
        self.Label5_2.configure(activeforeground="black")
        self.Label5_2.configure(anchor='e')
        self.Label5_2.configure(background="#d9d9d9")
        self.Label5_2.configure(disabledforeground="#a3a3a3")
        self.Label5_2.configure(foreground="#000000")
        self.Label5_2.configure(highlightbackground="#d9d9d9")
        self.Label5_2.configure(highlightcolor="black")
        self.Label5_2.configure(text='''Transaction ID Column :''')

        self.tf_TransactionID2 = tk.Entry(self.Labelframe1_1)
        self.tf_TransactionID2.place(x=150, y=130, height=20, width=34
                , bordermode='ignore')
        self.tf_TransactionID2.configure(background="white")
        self.tf_TransactionID2.configure(disabledforeground="#a3a3a3")
        self.tf_TransactionID2.configure(font="TkFixedFont")
        self.tf_TransactionID2.configure(foreground="#000000")
        self.tf_TransactionID2.configure(highlightbackground="#d9d9d9")
        self.tf_TransactionID2.configure(highlightcolor="black")
        self.tf_TransactionID2.configure(insertbackground="black")
        self.tf_TransactionID2.configure(selectbackground="blue")
        self.tf_TransactionID2.configure(selectforeground="white")

        self.Label5_1_2 = tk.Label(self.Labelframe1_1)
        self.Label5_1_2.place(x=30, y=160, height=21, width=114
                , bordermode='ignore')
        self.Label5_1_2.configure(activebackground="#f9f9f9")
        self.Label5_1_2.configure(activeforeground="black")
        self.Label5_1_2.configure(anchor='e')
        self.Label5_1_2.configure(background="#d9d9d9")
        self.Label5_1_2.configure(disabledforeground="#a3a3a3")
        self.Label5_1_2.configure(foreground="#000000")
        self.Label5_1_2.configure(highlightbackground="#d9d9d9")
        self.Label5_1_2.configure(highlightcolor="black")
        self.Label5_1_2.configure(text='''Product ID Column :''')

        self.tf_ProductID = tk.Entry(self.Labelframe1_1)
        self.tf_ProductID.place(x=150, y=160, height=20, width=34
                , bordermode='ignore')
        self.tf_ProductID.configure(background="white")
        self.tf_ProductID.configure(disabledforeground="#a3a3a3")
        self.tf_ProductID.configure(font="TkFixedFont")
        self.tf_ProductID.configure(foreground="#000000")
        self.tf_ProductID.configure(highlightbackground="#d9d9d9")
        self.tf_ProductID.configure(highlightcolor="black")
        self.tf_ProductID.configure(insertbackground="black")
        self.tf_ProductID.configure(selectbackground="blue")
        self.tf_ProductID.configure(selectforeground="white")

        self.Label5_1_2_1 = tk.Label(self.Labelframe1_1)
        self.Label5_1_2_1.place(x=200, y=160, height=21, width=134
                , bordermode='ignore')
        self.Label5_1_2_1.configure(activebackground="#f9f9f9")
        self.Label5_1_2_1.configure(activeforeground="black")
        self.Label5_1_2_1.configure(anchor='e')
        self.Label5_1_2_1.configure(background="#d9d9d9")
        self.Label5_1_2_1.configure(cursor="fleur")
        self.Label5_1_2_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1_2_1.configure(foreground="#000000")
        self.Label5_1_2_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1_2_1.configure(highlightcolor="black")
        self.Label5_1_2_1.configure(text='''Product Name Column :''')

        self.tf_ProductName = tk.Entry(self.Labelframe1_1)
        self.tf_ProductName.place(x=340, y=160, height=20, width=34
                , bordermode='ignore')
        self.tf_ProductName.configure(background="white")
        self.tf_ProductName.configure(disabledforeground="#a3a3a3")
        self.tf_ProductName.configure(font="TkFixedFont")
        self.tf_ProductName.configure(foreground="#000000")
        self.tf_ProductName.configure(highlightbackground="#d9d9d9")
        self.tf_ProductName.configure(highlightcolor="black")
        self.tf_ProductName.configure(insertbackground="black")
        self.tf_ProductName.configure(selectbackground="blue")
        self.tf_ProductName.configure(selectforeground="white")

        self.Label5_1_2_1_1 = tk.Label(self.Labelframe1_1)
        self.Label5_1_2_1_1.place(x=390, y=160, height=21, width=134
                , bordermode='ignore')
        self.Label5_1_2_1_1.configure(activebackground="#f9f9f9")
        self.Label5_1_2_1_1.configure(activeforeground="black")
        self.Label5_1_2_1_1.configure(anchor='e')
        self.Label5_1_2_1_1.configure(background="#d9d9d9")
        self.Label5_1_2_1_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1_2_1_1.configure(foreground="#000000")
        self.Label5_1_2_1_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1_2_1_1.configure(highlightcolor="black")
        self.Label5_1_2_1_1.configure(text='''Product Price Column :''')

        self.tf_ProductPrice = tk.Entry(self.Labelframe1_1)
        self.tf_ProductPrice.place(x=530, y=160, height=20, width=34
                , bordermode='ignore')
        self.tf_ProductPrice.configure(background="white")
        self.tf_ProductPrice.configure(disabledforeground="#a3a3a3")
        self.tf_ProductPrice.configure(font="TkFixedFont")
        self.tf_ProductPrice.configure(foreground="#000000")
        self.tf_ProductPrice.configure(highlightbackground="#d9d9d9")
        self.tf_ProductPrice.configure(highlightcolor="black")
        self.tf_ProductPrice.configure(insertbackground="black")
        self.tf_ProductPrice.configure(selectbackground="blue")
        self.tf_ProductPrice.configure(selectforeground="white")

        self.Label5_1_1_1 = tk.Label(self.Labelframe1_1)
        self.Label5_1_1_1.place(x=550, y=130, height=21, width=74
                , bordermode='ignore')
        self.Label5_1_1_1.configure(activebackground="#f9f9f9")
        self.Label5_1_1_1.configure(activeforeground="black")
        self.Label5_1_1_1.configure(anchor='e')
        self.Label5_1_1_1.configure(background="#d9d9d9")
        self.Label5_1_1_1.configure(cursor="fleur")
        self.Label5_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1_1_1.configure(foreground="#000000")
        self.Label5_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1_1_1.configure(highlightcolor="black")
        self.Label5_1_1_1.configure(text='''Start Row :''')

        self.tf_TLineStartRow = tk.Entry(self.Labelframe1_1)
        self.tf_TLineStartRow.place(x=630, y=130, height=20, width=34
                , bordermode='ignore')
        self.tf_TLineStartRow.configure(background="white")
        self.tf_TLineStartRow.configure(disabledforeground="#a3a3a3")
        self.tf_TLineStartRow.configure(font="TkFixedFont")
        self.tf_TLineStartRow.configure(foreground="#000000")
        self.tf_TLineStartRow.configure(highlightbackground="#d9d9d9")
        self.tf_TLineStartRow.configure(highlightcolor="black")
        self.tf_TLineStartRow.configure(insertbackground="black")
        self.tf_TLineStartRow.configure(selectbackground="blue")
        self.tf_TLineStartRow.configure(selectforeground="white")

        self.btn_Back = tk.Button(self)
        self.btn_Back.place(x=10, y=460, height=38, width=53)
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

        self.btn_Import = tk.Button(self)
        self.btn_Import.place(x=300, y=460, height=38, width=73)
        self.btn_Import.configure(activebackground="#ececec")
        self.btn_Import.configure(activeforeground="#000000")
        self.btn_Import.configure(background="#d9d9d9")
        self.btn_Import.configure(disabledforeground="#a3a3a3")
        self.btn_Import.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.btn_Import.configure(foreground="#000000")
        self.btn_Import.configure(highlightbackground="#d9d9d9")
        self.btn_Import.configure(highlightcolor="black")
        self.btn_Import.configure(pady="0")
        self.btn_Import.configure(text='''Import''')

        #configure buttons

        self.btn_TChoose.configure(command=lambda: self.open_T())
        self.btn_TLineChoose.configure(command=lambda: self.open_TLine())
        self.btn_Back.configure(command=lambda: controller.show_frame("Admin_Options"))
        self.btn_Import.configure(command=lambda: self.importCSV(controller))

    def open_T(self):
        self.tFilename = tk.filedialog.askopenfilename(initialdir = "../",title = "Select Transaction CSV File",filetypes = (("Saved File (*.csv)","*.csv"),("All Files (*.*)","*.*")))
        self.lbl_TFile.configure(text=self.tFilename)

        file = open(self.tFilename, 'r') #transactions.csv
        contents = file.readlines()
        file.close()

        self.lbl_TFirst.configure(text = str(contents[0]))

    def open_TLine(self):
        self.tLineFilename = tk.filedialog.askopenfilename(initialdir = "../",title = "Select Transaction Line CSV File",filetypes = (("Saved File (*.csv)","*.csv"),("All Files (*.*)","*.*")))
        self.lbl_TLineFile.configure(text=self.tLineFilename)

        file = open(self.tLineFilename, 'r') #transactionslines.csv
        contents = file.readlines()
        file.close()

        self.lbl_TLineFirst.configure(text = str(contents[0]))

    def importCSV(self, controller):
        controller.importcsvinfos(int(self.tf_TstartRow.get()),
                                int(self.tf_TLineStartRow.get()),
                                int(self.tf_TransactionID1.get()),
                                int(self.tf_Datetime.get()),
                                int(self.tf_CustomerID.get()),
                                int(self.tf_TransactionID2.get()),
                                int(self.tf_ProductID.get()),
                                int(self.tf_ProductName.get()),
                                int(self.tf_ProductPrice.get()),
                                self.tFilename,
                                self.tLineFilename)




