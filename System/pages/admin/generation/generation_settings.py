import tkinter as tk
from tkcalendar import *

class Generation_Settings(tk.Frame):

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

        label = tk.Label(topFrame, text="Record Generation Parameters", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        amountDayLbl = tk.Label(midFrame1, text="Amount of Days: ", font=controller.content_font)
        startingDayLbl = tk.Label(midFrame2, text="Starting Date: ", font=controller.content_font)
        distributionLbl = tk.Label(midFrame3, text="Customer Distribution: ", font=controller.content_font)

        amountDayLbl.pack(side="left", padx=(150,0))
        startingDayLbl.pack(side="left", padx=(150,0))
        distributionLbl.pack(side="left", padx=(150,0))

        self.amountDayEntry = tk.Entry(midFrame1, font=controller.content_font)
        self.cal = Calendar(midFrame2, selectmode = "day", year = 2021, month=1,day=1)

        self.amountDayEntry.pack(side="right", padx=(0,150))
        self.cal.pack(side="right", padx=(0,150))

        self.variable = tk.StringVar(midFrame3)
        self.variable.set("Uniform") # default value
        w = tk.OptionMenu(midFrame3, self.variable, "Uniform", "Normal", "Exponential")
        w.pack(side="right", padx=(0,150))

        doneBtn = tk.Button(midFrame4, text="Done", command=lambda: self.done(controller), font=controller.button_font, width=10,bg="#c8cfca")
        doneBtn.pack(pady=10)

        button1 = tk.Button(midFrame4, text="Back",
                           command=lambda: controller.show_frame("Admin_Options"), font=controller.button_font,bg="#c8cfca")
        button1.pack()


    def done(self, controller):
        controller.show_frame("Admin_Options")
        print(self.cal.get_date())
        controller.generationDays = self.amountDayEntry.get()
        controller.generationStartingDate = self.cal.get_date()
        controller.generationCustomerDistribution = self.variable.get()

        print(f"day: {controller.generationDays} | starting {controller.generationStartingDate} | dist {controller.generationCustomerDistribution}")

        controller.recordStatus = 1
        controller.frames["Generate_Record"].updateVisuals()