import tkinter as tk

class Product_Edit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        midFrame = tk.Frame(self)
        bottomFrame = tk.Frame(self)

        topFrame.pack(side="top", fill="x")
        midFrame.pack(fill="both",pady=(10,10))
        bottomFrame.pack(side="bottom", pady=50)

        label = tk.Label(topFrame, text="Edit Product", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)

        label = tk.Label(midFrame, text="//Table Here", font=controller.content_font)
        label.pack(side="top", fill="x", pady=50)


        button1 = tk.Button(bottomFrame, text="Back",
                           command=lambda: controller.show_frame("Product_Options"), font=controller.button_font,bg="#c8cfca")
        button1.pack()