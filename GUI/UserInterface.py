from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

global_image_list = [] # global image list to avoid the garbage collection 

class QrView:
    # TODO: Createa a destructor to cleanup global image list
    def __init__(self, parent : Frame, **kwargs):
        # Configure rows' weights
        for x in range(0,5):
            parent.rowconfigure(x,weight=1)

        # Add the elements to prompt the user to scan the generated QR image
        Label(parent, text="2FA GENERATION", font=("TkDefaultFont", 18)).grid(column=0, row=1)

        image = PhotoImage(file="./Images/qr-code.png").subsample(x=6, y=6)
        global_image_list.append(image)
        Label(parent, image=image).grid(column=0, row=2, rowspan=1)

        Button(parent, text="Generate QR", width="21").grid(column=0,row=3, sticky="n")

class TokenView:
    # TODO: Createa a destructor to cleanup global image list
    def __init__(self, parent : Frame, **kwargs):
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

class FileEncryption:
    def __init__(self, root):
        self.root = root

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
        btn1 = Button(self.root, text="ENCRYPT", fg="white", bg="#007BFF", font=("Helvetica", 12, "bold"), command=self.encrypt_clicked, width=15, relief="raised", bd=2)
        btn2 = Button(self.root, text="HOME", fg="white", bg="#28a745", font=("Helvetica", 12, "bold"), command=self.home_clicked, width=15, relief="raised", bd=2)

        btn1.grid(row=5, column=0, columnspan=2, pady=20)
        btn2.grid(row=6, column=0, columnspan=2, pady=10)

    def encrypt_clicked(self):
        # Placeholder for encrypt logic
        print("Encrypt button clicked")

    def home_clicked(self):
        # Placeholder for home button logic
        print("Home button clicked")