import tkinter as tk

class Start(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self)
        bottomFrame = tk.Frame(self)

        topFrame.pack(side="top", fill="both")
        bottomFrame.pack(pady=50)

        label = tk.Label(topFrame, text="GUI TEST TKINTER", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)


        button1 = tk.Button(bottomFrame, text="Admin",
                            command=lambda: controller.show_frame("Admin_Options"), font=controller.button_font,bg="#c8cfca")


        button2 = tk.Button(bottomFrame, text="User",
                            command=lambda: controller.show_frame("User_Options"), font=controller.button_font,bg="#c8cfca")
        button1.pack(side="left", padx=(0,10))
        button2.pack(side="right", padx=(10,0))