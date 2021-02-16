import tkinter as tk

class Generate_Record(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        midFrame = tk.Frame(self)
        midFrame2 =tk.Frame(self)
        bottomFrame = tk.Frame(self)

        topFrame.pack(side="top", fill="x")
        midFrame.pack(fill="both",pady=(10,10))
        midFrame2.pack(fill="x",pady=(10,10))
        bottomFrame.pack(side="bottom", pady=50)

        label = tk.Label(topFrame, text="Generate Transaction Records", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)
        
        setting1 = tk.Label(midFrame, text="Product Records Settings ", font=controller.content_font_bold)
        setting2 = tk.Label(midFrame, text="Customer Parameters Settings ", font=controller.content_font_bold)
        setting3 = tk.Label(midFrame, text="Store Parameters Settings ", font=controller.content_font_bold)
        setting4 = tk.Label(midFrame, text="Record Generation Settings ", font=controller.content_font_bold)
        setting1.grid(row=0, column=0, sticky="w", padx=50, pady=10)
        setting2.grid(row=1, column=0, sticky="w", padx=50, pady=10)
        setting3.grid(row=2, column=0, sticky="w", padx=50, pady=10)
        setting4.grid(row=3, column=0, sticky="w", padx=50, pady=10)

        

        self.status1 = tk.Label(midFrame, text="Incomplete ", font=controller.content_font, fg="Red")
        self.status2 = tk.Label(midFrame, text="Incomplete ", font=controller.content_font, fg="Red")
        self.status3 = tk.Label(midFrame, text="Incomplete ", font=controller.content_font, fg="Red")
        self.status4 = tk.Label(midFrame, text="Incomplete ", font=controller.content_font, fg="Red")
        self.status1.grid(row=0, column=2, sticky="w", padx=(0, 50))
        self.status2.grid(row=1, column=2, sticky="w", padx=(0, 50))
        self.status3.grid(row=2, column=2, sticky="w", padx=(0, 50))
        self.status4.grid(row=3, column=2, sticky="w", padx=(0, 50))
        midFrame.grid_columnconfigure(0,weight=1)

        option1 = tk.Button(midFrame2, text="Generate", command=lambda: self.gen(), font=controller.button_font, width=10,bg="#c8cfca")
        option1.pack(pady=10)

        button1 = tk.Button(midFrame2, text="Back",
                           command=lambda: controller.show_frame("Admin_Options"), font=controller.button_font,bg="#c8cfca")
        button1.pack()

        self.updateVisuals()


    def gen(self):
        if self.controller.productStatus == 0 or self.controller.customerStatus == 0 or self.controller.storeStatus == 0 or self.controller.recordStatus == 0:
            tk.messagebox.showinfo('Error','Steps is not completed')
        else:
            tk.messagebox.showinfo('Starting...','Generation starting...')
            self.controller.recordGenerator.generate()
            tk.messagebox.showinfo('Success','Generation completed, proceed to import')

    def updateVisuals(self):
        
        if self.controller.productStatus == 0:
            self.status1.configure(text="Incomplete")
            self.status1.configure(fg="Red")
        else:
            self.status1.configure(text="Completed")
            self.status1.configure(fg="Green")
        
        if self.controller.customerStatus == 0:
            self.status2.configure(text="Incomplete")
            self.status2.configure(fg="Red")
        else:
            self.status2.configure(text="Completed")
            self.status2.configure(fg="Green")
        
        if self.controller.storeStatus == 0:
            self.status3.configure(text="Incomplete")
            self.status3.configure(fg="Red")
        else:
            self.status3.configure(text="Completed")
            self.status3.configure(fg="Green")
        
        if self.controller.recordStatus == 0:
            self.status4.configure(text="Incomplete")
            self.status4.configure(fg="Red")
        else:
            self.status4.configure(text="Completed")
            self.status4.configure(fg="Green")