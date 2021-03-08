import tkinter as tk
from tkinter import font  as tkfont
from tkinter import filedialog
import os
from threading import Thread
from datetime import datetime, timedelta

# importing pages
from pages.start import Start
from pages.user.options import User_Options
from pages.admin.options import Admin_Options
from pages.user.simulationPage import SimPage

#individual pages import
from pages.admin.import_rec.admin_import import Admin_Import
from pages.admin.customer.customer_param import Customer_Param
from pages.admin.customer.customer_type_param1 import Customer_Type_Param1
from pages.admin.customer.customer_type_param2 import Customer_Type_Param2
from pages.admin.customer.customer_type_param3 import Customer_Type_Param3
from pages.admin.generate_rec.generate_record import Generate_Record
from pages.admin.generation.generation_settings import Generation_Settings
from pages.admin.product.product_options import Product_Options
from pages.admin.product.product_view import Product_View
from pages.admin.product.product_add import Product_Add
from pages.admin.product.product_edit import Product_Edit
from pages.admin.product.product_edit2 import Product_Edit2
from pages.admin.product.product_delete import Product_Delete
from pages.admin.store.store_settings import Store_Settings

#import objects
from objects.customer import Customer
from objects.products import Products
from objects.transaction import Transaction
from objects.transactionline import Transaction_Lines

#import modules
from modules.csvimport import Csv_Import
from modules.generate import Record_Generator
from modules.convertToJSON import Converter
from modules.simulation import Simulation

from tinydb import TinyDB

#Dictionary for lines

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #fonts
        self.title_font = tkfont.Font(family='Helvetica', size=30, weight="bold", slant="italic")
        self.button_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.content_font = tkfont.Font(family='Helvetica', size=13)
        self.content_font_bold = tkfont.Font(family='Helvetica', size=13, weight="bold")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("Customer Simulation System")
        self.geometry("700x500")
        self.resizable(False,False)

        self.frames = {}

        # transaction records objects
        self.json = {}

        '''
            ---- GENERATION VARIABLES ----
        '''

        # customer params
        self.customerAmount = 0
        self.customerTypesN = 1

        self.customerTypes = {"t1P": 0,
        "t1R": 0,
        "t2P": 0,
        "t2R": 0,
        "t3P": 0,
        "t3R": 0} # TODOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

        # store params
        self.storeStartHour = 0 #24 hour format
        self.storeCloseHour = 12
        self.storeOperationDays = [] #list of operation day

        # generation params
        self.generationDays = 0
        self.generationStartingDate = ""
        self.generationCustomerDistribution = "Uniform"
        #
        #
        #
        #
        #

        # product list for generation
        self.productList = []

        # customer list for generation
        self.customerList = []
        
        # record generator object

        self.recordGenerator = Record_Generator(self)

        '''
            ---- GENERATION VARIABLES END ----
        '''

        '''
            ---- GENERATION STATUS ----
        '''
        self.productStatus = 0
        self.customerStatus = 0
        self.storeStatus = 0
        self.recordStatus = 0

        '''
            ---- GENERATION STATUS END ----
        '''
        self.csvObj = Csv_Import()

        # Simulator objects
        self.simulator = Simulation(self)
        
        # Records for Simulation Object
        self.tdic = {}
        self.ldic = {}

        # all pages in app
        pages = []
        pages.append(Start)
        pages.append(Admin_Options)
        pages.append(User_Options)
        pages.append(Admin_Import)
        pages.append(Customer_Param)
        pages.append(Customer_Type_Param1)
        pages.append(Customer_Type_Param2)
        pages.append(Customer_Type_Param3)
        pages.append(Product_Options)
        pages.append(Product_Add)
        pages.append(Product_Edit)
        pages.append(Product_View)
        pages.append(Product_Delete)
        pages.append(Generate_Record)
        pages.append(Store_Settings)
        pages.append(Generation_Settings)
        pages.append(Product_Edit2)
        pages.append(SimPage)

        for F in pages:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Start")

        #Add dummy contents
        self.dummyFill()

        self.refreshTables()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)



    def dummyFill(self):
        #self.frames["Product_Add"].addProduct(self,"name","brand", 3.99)
        self.frames["Product_Add"].addProduct(self,"Carrot","Cameron", 1.9)
        self.frames["Product_Add"].addProduct(self,"Cabbage","Cameron", 2.9)
        self.frames["Product_Add"].addProduct(self,"Cauliflower","Cameron", 3.9)
        self.frames["Product_Add"].addProduct(self,"Whole Chicken","Ayamas", 8.9)
        self.frames["Product_Add"].addProduct(self,"Rice","Jati", 23.9)
        self.frames["Product_Add"].addProduct(self,"Cooking Oil","Knife", 23.5)
        self.frames["Product_Add"].addProduct(self,"Chilli Sauce","Life", 3.15)
        self.frames["Product_Add"].addProduct(self,"Boneless Chicken","Ayamas", 12.9)
        self.frames["Product_Add"].addProduct(self,"Rice","Jasmine", 27.9)
        self.frames["Product_Add"].addProduct(self,"Sardine","Marina", 6.5)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def on_closing(self):
        self.simulator.quitWindow()
        self.destroy()

        

    def sim(self):
        d = Thread(target=self.openprototype, args=())
        d.start()
        self.frames["SimPage"].clearLog()
        self.show_frame("SimPage")
        
    def simBack(self):
        self.simulator.quitWindow()
        self.show_frame("Start")

    def playtoggle(self):
        self.simulator.playPauseToggle()

    def open_Prev(self):
        self.filename = tk.filedialog.askopenfilename(initialdir = "../",title = "Select file",filetypes = (("Saved File (*.json)","*.json"),("All Files (*.*)","*.*")))
        db = TinyDB(self.filename)
        results = db.get(doc_id=1)
        
    def openprototype(self):
        self.simulator = Simulation(self)
        self.filename = tk.filedialog.askopenfilename(initialdir = "../",title = "Select file",filetypes = (("Saved File (*.json)","*.json"),("All Files (*.*)","*.*")))
        db = TinyDB(self.filename)
        results = db.get(doc_id=1)
        tlist = results["transactions"]
        llist = results["lines"]
        time = results["time"]
        self.simulator.startSim(tlist,llist,time)

    def importcsvinfos(self, tStartRow, lStartRow, tID, tDT, tCID, tID2, lIID, lI, lP, tDir, lDir):
        #print(f"{tStartRow}, {lStartRow}, {tID}, {tDT}, {tCID}, {tID2}, {lIID}, {lI}, {lP}, {tDir}, {lDir}")

        self.csvObj.setColumns(tStartRow, lStartRow, tID, tDT, tCID, tID2, lIID, lI, lP)
        
        self.tdic,self.ldic = self.csvObj.importcsv(tDir, lDir)

        #Convert to JSON here
        a = datetime.strptime(self.tdic[0]["datetime"], '%m/%d/%Y %I:%M %p')
        b = a - timedelta(minutes=30)

        c = Converter()
        json = c.convert(self.tdic, self.ldic, self.tdic[0]["datetime"])

        #------
        #save to directory as json
        f = tk.filedialog.asksaveasfile(mode='w', defaultextension=".json",filetypes = [("JSON File",".json")])
        savedirectory = f.name
        f.close()
        db = TinyDB(savedirectory)
        db.insert(json)

        

    def refreshTables(self):
        self.frames['Product_View'].refreshTable(self)
        self.frames['Product_Edit'].refreshTable(self)
        self.frames['Product_Delete'].refreshTable(self)
        self.productCheck()

    def productCheck(self):
        if len(self.productList) == 0:
            self.productStatus = 0
        else:
            self.productStatus = 1

        self.frames["Generate_Record"].updateVisuals()


    



if __name__ == "__main__":
    app = Main()
    app.mainloop()
