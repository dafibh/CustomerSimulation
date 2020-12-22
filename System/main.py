import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

from pages.start import Start
from pages.user_options import User_Options
from pages.admin_options import Admin_Options

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #fonts
        self.title_font = tkfont.Font(family='Helvetica', size=30, weight="bold", slant="italic")
        self.button_font = tkfont.Font(family='Helvetica', size=16, weight="bold")

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



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()