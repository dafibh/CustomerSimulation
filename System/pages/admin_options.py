import tkinter as tk

class Admin_Options(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        midFrame1 = tk.Frame(self)
        midFrame2 = tk.Frame(self)
        midFrame3 = tk.Frame(self)
        bottomFrame = tk.Frame(self)

        topFrame.pack(side="top", fill="x")
        midFrame1.pack(fill="both",pady=(10,10))
        midFrame2.pack(fill="both",pady=(10,10))
        midFrame3.pack(fill="x",pady=(10,10))
        bottomFrame.pack(side="bottom", pady=(0,10))

        label = tk.Label(topFrame, text="Admin Options", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)


        option1 = tk.Button(midFrame1, text="Product\nParameters", font=controller.button_font, width=10, height=2,bg="#c8cfca")
        option2 = tk.Button(midFrame1, text="Customer\nParameters", font=controller.button_font, width=10, height=2,bg="#c8cfca")
        option3 = tk.Button(midFrame2, text="Store\nParameters", font=controller.button_font, width=10, height=2,bg="#c8cfca")
        option4 = tk.Button(midFrame2, text="Generation\nParameters", font=controller.button_font, width=10, height=2,bg="#c8cfca")
        option5 = tk.Button(midFrame3, text="Generate\nRecords", font=controller.button_font, width=10, height=2,bg="#c8cfca")

        option1.pack(side="left",padx=(150,0))
        option2.pack(side="right",padx=(0,150))
        option3.pack(side="left",padx=(150,0))
        option4.pack(side="right",padx=(0,150))
        option5.pack()

        back = tk.Button(bottomFrame, text="Back",
                           command=lambda: controller.show_frame("Start"), font=controller.button_font,bg="#c8cfca")
        back.grid(row=0,column=0)