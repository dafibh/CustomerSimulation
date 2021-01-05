import tkinter as tk

class Customer_Type_Param(tk.Frame):

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

        label = tk.Label(topFrame, text="Customer Type Parameters", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)

        itemPurchaseLbl = tk.Label(midFrame1, text="Item Purchase Amount: ", font=controller.content_font)
        visitsLbl = tk.Label(midFrame2, text="Number Of Visit: [1 / >1 = Returning]   ", font=controller.content_font)
        itemPurchaseLbl.pack(side="left", padx=(150,0))
        visitsLbl.pack(side="left", padx=(150,0))

        itemPurchaseEntry = tk.Entry(midFrame1, font=controller.content_font)
        visitsEntry = tk.Entry(midFrame2, font=controller.content_font)
        itemPurchaseEntry.pack(side="right", padx=(0,150))
        visitsEntry.pack(side="right", padx=(0,150))

        
        doneBtn = tk.Button(midFrame3, text="Done", command=lambda: controller.show_frame("Admin_Options"), font=controller.button_font, width=10,bg="#c8cfca")
        doneBtn.pack()

        button1 = tk.Button(bottomFrame, text="Back",
                           command=lambda: controller.show_frame("Customer_Param"), font=controller.button_font,bg="#c8cfca")
        button1.pack()