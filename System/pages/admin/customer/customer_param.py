import tkinter as tk

class Customer_Param(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        midFrame1 = tk.Frame(self)
        midFrame2 = tk.Frame(self)
        midFrame3 = tk.Frame(self)
        bottomFrame = tk.Frame(self)

        topFrame.pack(side="top", fill="x")
        midFrame1.pack(fill="both",pady=(10,10))
        midFrame2.pack(fill="both",pady=(10,10))
        midFrame3.pack(fill="x",pady=(10,10))
        bottomFrame.pack(side="bottom", pady=50)

        label = tk.Label(topFrame, text="Customer Parameters", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)

        custAmountLbl = tk.Label(midFrame1, text="Customer Amount: [Customer Amount > 50] ", font=controller.content_font)
        custTypesLbl = tk.Label(midFrame2, text="Customer Types: [Customer Types, 1 to 3]   ", font=controller.content_font)
        custAmountLbl.pack(side="left", padx=(150,0))
        custTypesLbl.pack(side="left", padx=(150,0))

        self.custAmountEntry = tk.Entry(midFrame1, font=controller.content_font)
        self.custTypesEntry = tk.Entry(midFrame2, font=controller.content_font)
        self.custAmountEntry.pack(side="right", padx=(0,150))
        self.custTypesEntry.pack(side="right", padx=(0,150))

        
        nextBtn = tk.Button(midFrame3, text="Next", command=lambda: self.nextPage(), font=controller.button_font, width=10,bg="#c8cfca")
        nextBtn.pack()

        button1 = tk.Button(bottomFrame, text="Back",
                           command=lambda: controller.show_frame("Admin_Options"), font=controller.button_font,bg="#c8cfca")
        button1.pack()

    def getCustN(self):
        return self.custAmountEntry.get()

    def getTypeN(self):
        return self.custTypesEntry.get()

    def nextPage(self):

        if int(self.custAmountEntry.get()) < 50 or int(self.custTypesEntry.get())>3 or int(self.custTypesEntry.get()) < 1:
            # alert
            tk.messagebox.showinfo('Alert','Customer is less than 50 or Customer Types is not within range!')
        else:
            self.controller.customerAmount = int(self.getCustN())
            self.controller.customerTypesN = int(self.getTypeN())
            self.controller.show_frame("Customer_Type_Param1")

