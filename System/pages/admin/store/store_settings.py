import tkinter as tk

class Store_Settings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        midFrame = tk.Frame(self)
        m1 = tk.Frame(self)
        m2 = tk.Frame(self)
        m3 = tk.Frame(self)
        m4 = tk.Frame(self)
        m5 = tk.Frame(self)
        m6 = tk.Frame(self)

        bottomFrame = tk.Frame(self)

        topFrame.pack(side="top", fill="x")
        midFrame.pack(fill="both",pady=(10,10))
        bottomFrame.pack(side="bottom", pady=50)

        label = tk.Label(topFrame, text="Customer Parameters", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)

        l1 = tk.Label(midFrame, text= "1")
        l1.grid(row = 0, column = 1, sticky="nsew")
        l2 = tk.Label(midFrame, text= "2")
        l2.grid(row = 0, column = 2, sticky="nsew")
        l3 = tk.Label(midFrame, text= "3")
        l3.grid(row = 1, column = 1, sticky="nsew")
        l4 = tk.Label(midFrame, text= "4")
        l4.grid(row = 1, column = 2, sticky="nsew")
        l5 = tk.Label(midFrame, text= "5")
        l5.grid(row = 2, column = 1, sticky="nsew")
        l6 = tk.Label(midFrame, text= "6")
        l6.grid(row = 2, column = 2, sticky="nsew")

        midFrame.grid_columnconfigure(0, weight=1)
        midFrame.grid_columnconfigure(3, weight=1)

        #option1 = tk.Button(midFrame, text="Load\nPrevious\nSession", command=lambda: controller.open_Prev(), font=controller.button_font, width=10, height=5,bg="#c8cfca")
        #option2 = tk.Button(midFrame, text="Create\nNew\nSession", command=lambda: controller.sim(entry.get()), font=controller.button_font, width=10, height=5,bg="#c8cfca")
        #option1.pack(side="left",padx=(150,0))
        #option2.pack(side="right",padx=(0,150))

        button1 = tk.Button(bottomFrame, text="Back",
                           command=lambda: controller.show_frame("Start"), font=controller.button_font,bg="#c8cfca")
        button1.pack()