import tkinter as tk
from tkinter import *

class GUI:
    

    def loadGUI(self, master=None):
        root = tk.Tk()
        w = tk.Label(root, text="Gello")
        top_frame = self.createFrame("top", root)
        btn1 = tk.Button(top_frame, text = "Button1", fg = "red").pack()
        self.master = master
        w.pack()
        root.mainloop()
    

    def createFrame(self, placement, root):
        return tk.Frame(root).pack(side = placement)

        


    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)