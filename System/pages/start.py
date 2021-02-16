import tkinter as tk

class Start(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        bottomFrame = tk.Frame(self)

        topFrame.pack(side="top", fill="both")
        bottomFrame.pack(fill="both",pady=10)

        label = tk.Label(topFrame, text="Customer Simulation System", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)


        button1 = tk.Button(bottomFrame, text="Generate\nRecords",
                            command=lambda: controller.show_frame("Admin_Options"), font=controller.button_font, width=10, height=5,bg="#c8cfca")


        """button2 = tk.Button(bottomFrame, text="Simulation",
                            command=lambda: controller.show_frame("User_Options"), font=controller.button_font, width=10, height=5,bg="#c8cfca")"""
        
        button2 = tk.Button(bottomFrame, text="Simulation",
                            command=lambda: controller.sim(), font=controller.button_font, width=10, height=5,bg="#c8cfca")
        button1.pack(side="left", padx=(150,0))
        button2.pack(side="right", padx=(0,150))