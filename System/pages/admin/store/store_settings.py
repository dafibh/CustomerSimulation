import tkinter as tk
from tkinter import messagebox
class Store_Settings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        midFrame = tk.Frame(self)

        bottomFrame = tk.Frame(self)

        topFrame.pack(side="top", fill="x")
        midFrame.pack(fill="both",pady=(10,10))
        bottomFrame.pack(side="bottom", pady=50)

        label = tk.Label(topFrame, text="Store Parameters", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)

        operationHoursLbl = tk.Label(midFrame, text="Operation Hours", font=controller.content_font)
        operationDayLbl = tk.Label(midFrame, text="Operation Days", font=controller.content_font)
        operationHoursLbl.grid(row=0, column=1, sticky="w")
        operationDayLbl.grid(row=1, column=1, sticky="w")

        self.operationHoursEntry1 = tk.Entry(midFrame)
        self.operationHoursEntry1.grid(row=0, column=2)
        self.operationHoursEntry2 = tk.Entry(midFrame)
        self.operationHoursEntry2.grid(row=0, column=3)

        # variable for checks
        self.v1 = tk.IntVar()
        self.v2 = tk.IntVar()
        self.v3 = tk.IntVar()
        self.v4 = tk.IntVar()
        self.v5 = tk.IntVar()
        self.v6 = tk.IntVar()
        self.v7 = tk.IntVar()


        self.d1 = tk.Checkbutton(midFrame, text="Monday", variable=self.v1)
        self.d1.grid(row=1, column=2, sticky="w")
        self.d2 = tk.Checkbutton(midFrame, text="Tuesday", variable=self.v2)
        self.d2.grid(row=1, column=3, sticky="w")
        self.d3 = tk.Checkbutton(midFrame, text="Wednesday", variable=self.v3)
        self.d3.grid(row=2, column=2, sticky="w")
        self.d4 = tk.Checkbutton(midFrame, text="Thursday", variable=self.v4)
        self.d4.grid(row=2, column=3, sticky="w")
        self.d5 = tk.Checkbutton(midFrame, text="Friday", variable=self.v5)
        self.d5.grid(row=3, column=2, sticky="w")
        self.d6 = tk.Checkbutton(midFrame, text="Saturday", variable=self.v6)
        self.d6.grid(row=3, column=3, sticky="w")
        self.d7 = tk.Checkbutton(midFrame, text="Sunday", variable=self.v7)
        self.d7.grid(row=4, column=2, sticky="w")

        midFrame.grid_columnconfigure(0, weight=1)
        midFrame.grid_columnconfigure(4, weight=1)
        option1 = tk.Button(midFrame, text="Done", command=lambda: self.done(controller), font=controller.button_font, width=10,bg="#c8cfca")
        option1.grid(row=5, column=2, sticky="nsew")
        
        button1 = tk.Button(bottomFrame, text="Back",
                           command=lambda: controller.show_frame("Admin_Options"), font=controller.button_font,bg="#c8cfca")
        button1.pack()

    def done(self,controller):
        controller.show_frame("Admin_Options")
        controller.storeOperationDays.clear()

        if self.v1.get()==1:
            controller.storeOperationDays.append("Monday")
        if self.v2.get()==1:
            controller.storeOperationDays.append("Tuesday")
        if self.v3.get()==1:
            controller.storeOperationDays.append("Wednesday")
        if self.v4.get()==1:
            controller.storeOperationDays.append("Thursday")
        if self.v5.get()==1:
            controller.storeOperationDays.append("Friday")
        if self.v6.get()==1:
            controller.storeOperationDays.append("Saturday")
        if self.v7.get()==1:
            controller.storeOperationDays.append("Sunday")

        controller.storeStartHour = self.operationHoursEntry1.get()
        controller.storeCloseHour = self.operationHoursEntry2.get()
        controller.storeStatus = 1
        controller.frames["Generate_Record"].updateVisuals()

        