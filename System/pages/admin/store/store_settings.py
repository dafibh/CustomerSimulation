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
        entry = tk.Entry(bottomFrame)
        option1 = tk.Button(midFrame, text="Load\nPrevious\nSession", command=lambda: controller.open_Prev(), font=controller.button_font, width=10, height=5,bg="#c8cfca")
        option2 = tk.Button(midFrame, text="Create\nNew\nSession", command=lambda: controller.sim(entry.get()), font=controller.button_font, width=10, height=5,bg="#c8cfca")
        entry.pack()
        option1.pack(side="left",padx=(150,0))
        option2.pack(side="right",padx=(0,150))

        button1 = tk.Button(bottomFrame, text="Back",
                           command=lambda: controller.show_frame("Start"), font=controller.button_font,bg="#c8cfca")
        button1.pack()