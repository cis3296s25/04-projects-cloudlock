from GUI import UserInterface as ui
from tkinter import *
from tkinter import ttk

# Setup our root and declare its size
root = Tk()
root.title("Complete 2FA")
root.geometry("400x500")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.grid()

ui.QrView(root)
# ui.TokenView(root)
# ui.FileEncryption(root)
# ui.Cloud(root)

root.mainloop()