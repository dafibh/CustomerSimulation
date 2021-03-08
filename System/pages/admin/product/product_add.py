import tkinter as tk
from objects.products import Products

class Product_Add(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        midFrame1 = tk.Frame(self)
        midFrame2 = tk.Frame(self)
        midFrame3 = tk.Frame(self)
        midFrame4 = tk.Frame(self)
        bottomFrame = tk.Frame(self)

        topFrame.pack(side="top", fill="x")
        midFrame1.pack(fill="both",pady=(10,10))
        midFrame2.pack(fill="both",pady=(10,10))
        midFrame3.pack(fill="both",pady=(10,10))
        midFrame4.pack(fill="x",pady=(10,10))
        bottomFrame.pack(side="bottom", pady=50)

        label = tk.Label(topFrame, text="Add New Product", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)

        nameLbl = tk.Label(midFrame1, text="Product Name: ", font=controller.content_font)
        brandLbl = tk.Label(midFrame2, text="Product Brand: ", font=controller.content_font)
        priceLbl = tk.Label(midFrame3, text="Price (RM): ", font=controller.content_font)

        nameLbl.pack(side="left", padx=(150,0))
        brandLbl.pack(side="left", padx=(150,0))
        priceLbl.pack(side="left", padx=(150,0))

        self.nameEntry = tk.Entry(midFrame1, font=controller.content_font)
        self.brandEntry = tk.Entry(midFrame2, font=controller.content_font)
        self.priceEntry = tk.Entry(midFrame3, font=controller.content_font)

        self.nameEntry.pack(side="right", padx=(0,150))
        self.brandEntry.pack(side="right", padx=(0,150))
        self.priceEntry.pack(side="right", padx=(0,150))

        doneBtn = tk.Button(midFrame4, text="Add Product", font=controller.button_font, width=10,bg="#c8cfca")
        doneBtn.configure(command=lambda: self.addProduct(controller, self.nameEntry.get(), self.brandEntry.get(), self.priceEntry.get()))
        doneBtn.pack()

        button1 = tk.Button(bottomFrame, text="Back",
                           command=lambda: controller.show_frame("Product_Options"), font=controller.button_font,bg="#c8cfca")
        button1.pack()

    def addProduct(self,controller, name, brand, price):

        if len(controller.productList) == 0:
            id = 0
        else:
            id = controller.productList[len(controller.productList)-1].getID() + 1
        
        controller.productList.append(Products(id, name, brand, float(price)))

        self.nameEntry.delete(0,tk.END)
        self.brandEntry.delete(0,tk.END)
        self.priceEntry.delete(0,tk.END)

        controller.refreshTables()