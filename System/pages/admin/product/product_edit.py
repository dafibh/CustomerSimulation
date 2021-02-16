import tkinter as tk
from tkinter import ttk as ttk
class Product_Edit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        midFrame = tk.Frame(self)
        bottomFrame = tk.Frame(self)

        topFrame.pack(side="top", fill="x")
        midFrame.pack(fill="both",pady=(10,10))
        bottomFrame.pack(side="bottom", pady=10)

        label = tk.Label(topFrame, text="Edit Product", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)

        #Table

        self.table = ttk.Treeview(midFrame)
        #columns
        self.table['columns'] = ('id', 'brand', 'name', 'price')

        #format column
        self.table.column('#0', width=0, stretch=tk.NO)
        self.table.column('id', anchor=tk.W, minwidth = 25, width = 50)
        self.table.column('brand', anchor=tk.W, minwidth = 25)
        self.table.column('name', anchor=tk.W, minwidth = 25)
        self.table.column('price', anchor=tk.W, minwidth = 25)

        #headings
        self.table.heading('#0', text='', anchor=tk.W)
        self.table.heading('id',text = 'ID',anchor=tk.W)
        self.table.heading('brand',text = 'Brand',anchor=tk.W)
        self.table.heading('name',text ='Name',anchor=tk.W)
        self.table.heading('price',text ='Price',anchor=tk.W)
        
        #pack
        self.table.bind("<Double-1>", self.OnDoubleClick)
        self.table.pack(pady=10)


        button1 = tk.Button(bottomFrame, text="Back",
                           command=lambda: controller.show_frame("Product_Options"), font=controller.button_font,bg="#c8cfca")
        button1.pack()

    def refreshTable(self, controller):
        self.table.delete(*self.table.get_children())

        for i in controller.productList:
            self.table.insert(parent='', index='end', text='', values=(i.getID(),i.getBrand(),i.getName(),i.getPrice()))

    def OnDoubleClick(self, event):
        curItem = self.table.focus()
        id = self.table.item(curItem)['values'][0]
        self.controller.show_frame("Product_Edit2")
        self.controller.frames['Product_Edit2'].selection(id)
