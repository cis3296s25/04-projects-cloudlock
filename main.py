from GUI import UserInterface as ui
from tkinter import *
from tkinter import ttk

# Setup our root and declare its size
root = Tk()
root.title("Complete 2FA")
root.geometry("400x500")
root.minsize(width=200, height=400)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.grid()

# Holder will contain all the elements
holder = Frame(root)
# holder.place(relx=0.5, rely=0.5, relheight=1, anchor="center")
holder.grid(sticky="nesw")
holder.columnconfigure(0, weight=1)

ui.QrView(root)



root.mainloop()