"Collection of classes to display user interface"
import tkinter
from tkinter import *
#from tkinter import ttk, * imports everything
from PIL import ImageTk, Image
from BackEnd.Microsoft_Auth import authenticate_acct, create_one_time_password

global_image_list = [] # global image list to avoid the garbage collection 

def changeView(root : Frame, view):
    for child in root.winfo_children():
        child.destroy()
    view(root)

class QrView:
    "Accepts: callback"
    # TODO: Createa a destructor to cleanup global image list
    def __init__(self, parent : Frame, **kwargs):
        self.callback = kwargs.get("callback", None)
        self.username = tkinter.StringVar()
        text_variable = tkinter.StringVar()
        # Configure rows' weights
        for x in range(0,5):
            parent.rowconfigure(x,weight=1)

        # Add the elements to prompt the user to scan the generated QR image
        Label(parent, text="2FA GENERATION", font=("TkDefaultFont", 18)).grid(column=0, row=1)

        image = PhotoImage(file="./Images/qr-code.png").subsample(x=6, y=6)
        global_image_list.append(image)
        Label(parent, image=image).grid(column=0, row=2, rowspan=1)

        Label(parent, text="Microsoft Authentication Username", font=("TkDefaultFont", 12)).grid(column=0, row=3)
        Entry(parent, textvariable = text_variable, font=("TkDefaultFont", 12)).grid(column=0, row=4)
        self.username = text_variable.get()

        Button(parent, text="Authenticate code", width="21", command=lambda: self.button_clicked()).grid(
            column=0, row=5, sticky="n")

    def button_clicked(self):
        #TODO: work out how to send username to backend so that it can display the qr code when the
        #TODO: button is clicked.
        authenticate_acct(self.username)

        image = PhotoImage("./Images/qr-code.png".subsample(x=6, y=6))
        global_image_list.append(image)
        Label(self.root_frame, image=image).grid(column=0, row=2, rowspan=1)

        #creates user acct for the microsoft authentication. Then it creates the qr_code
        #if self.callback != None:
            #self.callback()
        #print("Button clicked")

class TokenView:
    "Accepts: callback"
    # TODO: Createa a destructor to cleanup global image list
    def __init__(self, parent : Frame, **kwargs):
        self.qrCode = StringVar()
        self.username = StringVar()
        self.root_frame = parent
        self.callback = kwargs.get("callback", None)

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

        Label(loginFrame, text="2FA - Token", font=("TkDefaultFont", 12)).grid(column=0, row=1)
        Entry(loginFrame, textvariable=self.qrCode, font=("TkDefaultFont", 12)).grid(column=1, row=1)

        Button(loginFrame, text="Log In", font=("TkDefaultFont", 12), command= lambda : self.button_clicked()).grid(column=0, row=2, columnspan=2)

    def button_clicked(self):
        #TODO: Make sure that when user inputs code, stuff gets sent to backend and actually verifies it
        #TODO: before changing the view to the "home page"
        to_verify = create_one_time_password()

        if(to_verify.verify(self.qrCode) != False): #take the code inout by user, compare it to TOTP created
            print("Correct code!")
            #changeView(self.root_frame, HomeView)

        #print(self.get_qr_text())
        #if self.callback != None:
        #    self.callback()
        #print("Button clicked")

    def get_qr_text(self):
        return self.qrCode.get()


class FileEncryption:
    "Accepts: home_callback, encryption_callback"
    def __init__(self, root, **kwargs):
        self.root = root
        self.encrypt_callback = kwargs.get("encrypt_callback")
        self.home_callback = kwargs.get("home_callback")

        # Call methods to create UI elements
        self.create_title_label()
        self.create_file_path_entry()
        self.create_file_name_entry()
        self.create_file_key_entry()
        self.create_file_desc_entry()
        self.create_buttons()

    # Method Definitions
    def create_title_label(self):
        title_lbl = Label(self.root, text='File Encryption System', font=("Helvetica", 16, "bold"), fg="#333", bg="#f0f0f0")
        title_lbl.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    def create_file_path_entry(self):
        file_path_lbl = Label(self.root, text="File Path:", font=("Helvetica", 12), bg="#f0f0f0")
        self.file_path_entry = Entry(self.root, width=40, font=("Helvetica", 12), bd=2, relief="solid")
        file_path_lbl.grid(row=1, column=0, pady=5, sticky="e")
        self.file_path_entry.grid(row=1, column=1, pady=5)

    def create_file_name_entry(self):
        file_name_lbl = Label(self.root, text="File Name:", font=("Helvetica", 12), bg="#f0f0f0")
        self.file_name_entry = Entry(self.root, width=40, font=("Helvetica", 12), bd=2, relief="solid")
        file_name_lbl.grid(row=2, column=0, pady=5, sticky="e")
        self.file_name_entry.grid(row=2, column=1, pady=5)

    def create_file_key_entry(self):
        file_key_lbl = Label(self.root, text="File Key:", font=("Helvetica", 12), bg="#f0f0f0")
        self.file_key_entry = Entry(self.root, width=40, font=("Helvetica", 12), bd=2, relief="solid")
        file_key_lbl.grid(row=3, column=0, pady=5, sticky="e")
        self.file_key_entry.grid(row=3, column=1, pady=5)

    def create_file_desc_entry(self):
        file_desc_lbl = Label(self.root, text="File Description:", font=("Helvetica", 12), bg="#f0f0f0")
        self.file_desc_entry = Entry(self.root, width=40, font=("Helvetica", 12), bd=2, relief="solid")
        file_desc_lbl.grid(row=4, column=0, pady=5, sticky="e")
        self.file_desc_entry.grid(row=4, column=1, pady=5)

    def create_buttons(self):
        btn1 = Button(self.root, text="ENCRYPT", fg="white", bg="#007BFF", font=("Helvetica", 12, "bold"), command= lambda : self.encrypt_clicked(), width=15, relief="raised", bd=2)
        btn2 = Button(self.root, text="HOME", fg="white", bg="#28a745", font=("Helvetica", 12, "bold"), command= lambda : self.home_clicked(), width=15, relief="raised", bd=2)

        btn1.grid(row=5, column=0, columnspan=2, pady=20)
        btn2.grid(row=6, column=0, columnspan=2, pady=10)

    def encrypt_clicked(self):
        if self.encrypt_callback != None:
            self.callback()
        # Placeholder for encrypt logic
        print("Encrypt button clicked")

    def home_clicked(self, **kwargs):
        if self.home_callback != None:
            self.callback()
        # Placeholder for home button logic
        print("Home button clicked")

class HomeView:
    #TODO: ADD OPTIONS FOR USER TO PICK WHAT TO DO AFTER THEY HAVE LOGGED IN
    def __init__(self, root, **kwargs):
        self.root = root