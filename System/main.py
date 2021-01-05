import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import filedialog
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
import os
from threading import Thread

# importing pages
from pages.start import Start
from pages.user.options import User_Options
from pages.admin.options import Admin_Options

from pages.admin.import_rec.admin_import import Admin_Import
from pages.admin.customer.customer_param import Customer_Param
from pages.admin.customer.customer_type_param import Customer_Type_Param
from pages.admin.generate_rec.generate_record import Generate_Record
from pages.admin.generation.generation_settings import Generation_Settings
from pages.admin.product.product_options import Product_Options
from pages.admin.product.product_view import Product_View
from pages.admin.product.product_add import Product_Add
from pages.admin.product.product_edit import Product_Edit
from pages.admin.product.product_delete import Product_Delete
from pages.admin.store.store_settings import Store_Settings
#from pages.admin. import 
#from pages.admin. import 
#from pages.admin. import 
#from pages.admin. import 

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #fonts
        self.title_font = tkfont.Font(family='Helvetica', size=30, weight="bold", slant="italic")
        self.button_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.content_font = tkfont.Font(family='Helvetica', size=13)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("Test")
        self.geometry("700x500")
        self.resizable(False,False)

        self.frames = {}

        # all pages in app
        pages = []
        pages.append(Start)
        pages.append(Admin_Options)
        pages.append(User_Options)
        pages.append(Admin_Import)
        pages.append(Customer_Param)
        pages.append(Customer_Type_Param)
        pages.append(Product_Options)
        pages.append(Product_Add)
        pages.append(Product_Edit)
        pages.append(Product_View)
        pages.append(Product_Delete)
        pages.append(Generate_Record)
        pages.append(Store_Settings)
        pages.append(Generation_Settings)

        for F in pages:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Start")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def sim(self):
        d = Thread(target=gg, args=())
        d.start()
        

    def open_Prev(self):
        self.filename = tk.filedialog.askopenfilename(initialdir = "../",title = "Select file",filetypes = (("Saved File (*.json)","*.json"),("All Files (*.*)","*.*")))
        print(self.filename)
        
def gg():
    os.system("python C:/Users/Duffy/Desktop/FYP/Project/CustomerSimulation/Prototype/sub_prototype.py")



if __name__ == "__main__":
    app = Main()
    app.mainloop()
