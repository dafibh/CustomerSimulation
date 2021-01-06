import tkinter as tk

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

        nameEntry = tk.Entry(midFrame1, font=controller.content_font)
        brandEntry = tk.Entry(midFrame2, font=controller.content_font)
        priceEntry = tk.Entry(midFrame3, font=controller.content_font)

        nameEntry.pack(side="right", padx=(0,150))
        brandEntry.pack(side="right", padx=(0,150))
        priceEntry.pack(side="right", padx=(0,150))

        doneBtn = tk.Button(midFrame4, text="Add Product", command=lambda: controller.show_frame("Product_Options"), font=controller.button_font, width=10,bg="#c8cfca")
        doneBtn.pack()

        button1 = tk.Button(bottomFrame, text="Back",
                           command=lambda: controller.show_frame("Product_Options"), font=controller.button_font,bg="#c8cfca")
        button1.pack()