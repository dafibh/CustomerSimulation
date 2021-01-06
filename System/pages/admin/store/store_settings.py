import tkinter as tk

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

        label = tk.Label(topFrame, text="Customer Parameters", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)

        operationHoursLbl = tk.Label(midFrame, text="Operation Hours", font=controller.content_font)
        operationDayLbl = tk.Label(midFrame, text="Operation Days", font=controller.content_font)
        operationHoursLbl.grid(row=0, column=1, sticky="w")
        operationDayLbl.grid(row=1, column=1, sticky="w")

        operationHoursEntry1 = tk.Entry(midFrame)
        operationHoursEntry1.grid(row=0, column=2)
        operationHoursEntry2 = tk.Entry(midFrame)
        operationHoursEntry2.grid(row=0, column=3)

        d1 = tk.Checkbutton(midFrame, text="Monday", variable=1)
        d1.grid(row=1, column=2, sticky="w")
        d2 = tk.Checkbutton(midFrame, text="Tuesday")
        d2.grid(row=1, column=3, sticky="w")
        d3 = tk.Checkbutton(midFrame, text="Wednesday")
        d3.grid(row=2, column=2, sticky="w")
        d4 = tk.Checkbutton(midFrame, text="Thursday")
        d4.grid(row=2, column=3, sticky="w")
        d5 = tk.Checkbutton(midFrame, text="Friday")
        d5.grid(row=3, column=2, sticky="w")
        d6 = tk.Checkbutton(midFrame, text="Saturday")
        d6.grid(row=3, column=3, sticky="w")
        d7 = tk.Checkbutton(midFrame, text="Sunday")
        d7.grid(row=4, column=2, sticky="w")

        midFrame.grid_columnconfigure(0, weight=1)
        midFrame.grid_columnconfigure(4, weight=1)
        option1 = tk.Button(midFrame, text="Done", command=lambda: controller.show_frame("Admin_Options"), font=controller.button_font, width=10,bg="#c8cfca")
        option1.grid(row=5, column=2, sticky="nsew")
        
        button1 = tk.Button(bottomFrame, text="Back",
                           command=lambda: controller.show_frame("Admin_Options"), font=controller.button_font,bg="#c8cfca")
        button1.pack()