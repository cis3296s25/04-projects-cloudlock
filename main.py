from GUI import UserInterface as ui
from tkinter import *
from tkinter import Tk

# Setup our root and declare its size
root = Tk()
root.title("Complete 2FA")
root.geometry("400x500")
root.minsize(width=400, height=500)
root.maxsize(width=400, height=500)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.grid()

# Holder will contain all the elements
holder = Frame(root)
holder.columnconfigure(0, weight=1)
holder.rowconfigure(0, weight=1)
holder.grid(sticky="nesw")

ui.QrView(root)
# ui.FileEncryption(root)
# ui.TokenView(root)
# ui.DownloadView(root)
# ui.Cloud(root)

root.mainloop()