from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

global_image_list = [] # global image list to avoid the garbage collection 

class QrView(Frame):
    # TODO: Createa a destructor to cleanup global image list
    def __init__(self, parent : Frame, *args):
        # Configure rows' weights
        for x in range(0,5):
            parent.rowconfigure(x,weight=1)

        # Add the elements to prompt the user to scan the generated QR image
        Label(parent, text="2FA GENERATION", font=("TkDefaultFont", 18)).grid(column=0, row=1)

        image = PhotoImage(file="./Images/qr-code.png").subsample(x=6, y=6)
        global_image_list.append(image)
        Label(parent, image=image).grid(column=0, row=2, rowspan=1)

        Button(parent, text="Generate QR", width="21").grid(column=0,row=3, sticky="n")

class TokenView(Frame):
    # TODO: Createa a destructor to cleanup global image list
    def __init__(self, parent : Frame, *args):
        qrCode = StringVar()
        # Configure rows' and columns' weights
        for x in range(0,5):
            parent.rowconfigure(x,weight=1)
            parent.columnconfigure(x, weight=1)

        Label(parent, text="2FA Authentication", font=("TkDefaultFont", 18)).grid(column=2, sticky="ns")

        # Create image using PIL (required for .jpg files)
        image = Image.open("./Images/2fa.jpg")
        image = image.resize((300,200))
        image= ImageTk.PhotoImage(image)
        global_image_list.append(image)

        Label(parent).grid(column=2, row=1, columnspan=1, sticky="n")

        # Create another frame to hold the information
        loginFrame = Frame(parent)
        loginFrame.grid(column=2, row=2, sticky="nesw", rowspan=5)
        
        # Setup the rows and columns in the loginFrame
        for x in range(0,5):
            loginFrame.rowconfigure(x, weight=1)
            loginFrame.columnconfigure(x, weight=1)

        Label(loginFrame, text="2FA - Token", font=("TkDefaultFont", 12)).grid(column=0, row=0)

        Entry(loginFrame, textvariable=qrCode, font=("TkDefaultFont", 12)).grid(column=1, row=0)

        Button(loginFrame, text="Log In", font=("TkDefaultFont", 12), command=lambda : command2(parent)).grid(column=0, row=1, columnspan=2)


