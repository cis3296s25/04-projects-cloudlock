<<<<<<< Updated upstream
=======
"Collection of classes to display user interface"
import tkinter
>>>>>>> Stashed changes
from tkinter import *
#from tkinter import ttk, * imports everything
from PIL import ImageTk, Image

from BackEnd.Microsoft_Auth import authenticate_acct

global_image_list = [] # global image list to avoid the garbage collection 

class QrView(Frame):
    # TODO: Createa a destructor to cleanup global image list
    # TODO: only post qr_code after AuthenticateView (AuthenticateView is untested)
    def __init__(self, parent : Frame, **kwargs):
        self.callback = kwargs.get("callback", None)
        text_variable = tkinter.StringVar()
        # Configure rows' weights
        for x in range(0,5):
            parent.rowconfigure(x,weight=1)

        qr_frame = Frame(parent)

        # Add the elements to prompt the user to scan the generated QR image
        Label(parent, text="2FA GENERATION", font=("TkDefaultFont", 18)).grid(column=0, row=1)

        image = PhotoImage(file="./Images/qr-code.png").subsample(x=6, y=6)
        global_image_list.append(image)
        Label(parent, image=image).grid(column=0, row=2, rowspan=1)
        Label(parent, text="Microsoft Authentication Username", font=("TkDefaultFont", 18)).grid(column=0, row=5)
        Entry(qr_frame, textvariable=text_variable, font=("TkDefaultFont", 12)).grid(column=1, row=0)

        Button(parent, text="Generate QR", width="21", command=lambda: self.button_clicked()).grid(
            column=0, row=3, sticky="n")


    def button_clicked(self):
        if self.callback != None:
            self.callback()
        print("Button clicked")

class AuthenticateView:
    "Accepts: callback"
    # TODO: Creata destructor to cleanup global image list

    def __init__(self, parent : Frame, **kwargs):
        self.callback = kwargs.get("callback", None)
        self.username = StringVar()
        self.code = StringVar()

        # Configure rows' and columns' weights
        for x in range(0, 5):
            parent.rowconfigure(x, weight=1)
            parent.columnconfigure(x, weight=1)

        Label(parent).grid(column=2, row=1, columnspan=1, sticky="n")

        authenticate_frame = Frame(parent)
        authenticate_frame.grid(column=2, row=2, sticky="nesw", rowspan=5)

        for x in range(0,5):
            authenticate_frame.rowconfigure(x, weight=1)
            authenticate_frame.columnconfigure(x, weight=1)

        Label(authenticate_frame, text="Enter username", font=("TkDefaultFont", 12)).grid(column=0, row=0)
        Entry(authenticate_frame, textvariable=self.username, font=("TkDefaultFont", 12)).grid(column=1, row=0)

        Label(authenticate_frame, text="Enter code", font=("TkDefaultFont", 12)).grid(column=0, row=1)
        Entry(authenticate_frame, textvariable=self.code, font=("TkDefaultFont", 12)).grid(column=1, row=1)
        Button(authenticate_frame, text="Submit", font=("TkDefaultFont", 12), command=lambda: self.button_clicked()).grid(
            column=0, row=2, columnspan=2)

    def button_clicked(self):
        to_verify = authenticate_acct(self.username)

        if(to_verify.verify(self.code)):
            #if it's true
            #https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
            #IN HERE IT SHOULD CALL QR CODE
            print("True, correct code")
        else:
            print("False >:(")


class TokenView:
    "Accepts: callback"
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

class FileSearch(Frame):
    def __init__(self, frame):
        # using helvetica for more modern look
        font_label = ("Helvetica", 12)
        font_entry = ("Helvetica", 12)
        font_button = ("Helvetica", 12, "bold")

        # creating title
        title_lbl = Label(frame, text='File Encryption System', font=("Helvetica", 16, "bold"), fg="#333", bg="#f0f0f0")
        title_lbl.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # file path entry
        file_path_lbl = Label(frame, text="File Path:", font=font_label, bg="#f0f0f0")
        file_path_entry = Entry(frame, width=40, font=font_entry, bd=2, relief="solid")
        file_path_lbl.grid(row=1, column=0, pady=5, sticky="e")
        file_path_entry.grid(row=1, column=1, pady=5)

        # file naame entry
        file_name_lbl = Label(frame, text="File Name:", font=font_label, bg="#f0f0f0")
        file_name_entry = Entry(frame, width=40, font=font_entry, bd=2, relief="solid")
        file_name_lbl.grid(row=2, column=0, pady=5, sticky="e")
        file_name_entry.grid(row=2, column=1, pady=5)

        # file key entry
        file_key_lbl = Label(frame, text="File Key:", font=font_label, bg="#f0f0f0")
        file_key_entry = Entry(frame, width=40, font=font_entry, bd=2, relief="solid")
        file_key_lbl.grid(row=3, column=0, pady=5, sticky="e")
        file_key_entry.grid(row=3, column=1, pady=5)

        # file description entry
        file_desc_lbl = Label(frame, text="File Description:", font=font_label, bg="#f0f0f0")
        file_desc_entry = Entry(frame, width=40, font=font_entry, bd=2, relief="solid")
        file_desc_lbl.grid(row=4, column=0, pady=5, sticky="e")
        file_desc_entry.grid(row=4, column=1, pady=5)

        # function to display entry values
        def clicked():
            file_name = file_name_entry.get()
            file_key = file_key_entry.get()
            file_desc = file_desc_entry.get()
            print(f"File Name: {file_name}, File Key: {file_key}, File Description: {file_desc}")

        # buttons for ENCRYPT and HOME
        btn1 = Button(frame, text="ENCRYPT", fg="white", bg="#007BFF", font=font_button, command=clicked, width=15, relief="raised", bd=2)
        btn2 = Button(frame, text="HOME", fg="white", bg="#28a745", font=font_button, command=clicked, width=15, relief="raised", bd=2)

        # position buttons below entries, centered
        btn1.grid(row=5, column=0, columnspan=2, pady=20)
        btn2.grid(row=6, column=0, columnspan=2, pady=10)