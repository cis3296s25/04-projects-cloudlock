import tkinter.filedialog as fd
from tkinter import Tk
import os

file = "hello"

class NewFileDialog(fd.FileDialog):
    def __init__(self, root):
        super().__init__(root)

root = Tk()

a = NewFileDialog(root)
a.set_filter(os.curdir, "*")

root.mainloop()