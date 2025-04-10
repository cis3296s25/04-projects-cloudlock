"Collection of classes to display user interface"
import tkinter as tk
from tkinter import *
from turtle import width
#* imports everything
from PIL import ImageTk, Image
from BackEnd.Microsoft_Auth import authenticate_acct, create_one_time_password, verify_user_code
import BackEnd.file_search as fs
import BackEnd.file_process as fp
import BackEnd.Generate_Qr as qr

global_image_list = {} # global image dictionary to avoid the garbage collection 
current_frame = None

def changeView(root : tk.Frame, view):
    for child in root.winfo_children():
        child.destroy()
    view(root)

class QrView:
    "Accepts: callback"
    # TODO: Createa a destructor to cleanup global image list
    def __init__(self, parent : tk.Frame, **kwargs):
        self.name = "qrview"
        current_frame = self.name # Set the current frame name to qrview
        self.callback = kwargs.get("callback", None)
        self.root_frame = parent
        text_variable = StringVar()

        # Configure rows' weights
        for x in range(0,5):
            parent.rowconfigure(x,weight=1, uniform="row")
            parent.columnconfigure(x,weight=1)

        # Add the elements to prompt the user to scan the generated QR image
        tk.Label(parent, text="2FA GENERATION", font=("TkDefaultFont", 18)).grid(row=0,column=0)

        self.qrImage = tk.Label(self.root_frame, width=2, height=2)
        self.qrImage.grid(column=0, row=1, sticky="news")

        tk.Label(parent, text="Microsoft Authentication Username", font=("TkDefaultFont", 18)).grid(row=2,column=0)
        tk.Entry(parent, textvariable=text_variable, font=("TkDefaultFont", 12)).grid(row=3, column=0)

        self.generate_widget = tk.Button(parent, text="Generate QR", width="20", command=lambda: self.button_clicked_generate(text_variable))
        self.generate_widget.grid(row=4, column=0, sticky="n")

        # If we already have a stored image, load it back
        if "QrImage" in global_image_list:
            self.qrImage.configure(image=global_image_list["QrImage"])
            self.generate_auth_button()

    def button_clicked_generate(self, username):
        authenticate_acct(username.get())
        self.generate_qr_image()
        self.generate_auth_button()

    def button_clicked_auth(self):
        changeView(self.root_frame, TokenView)

    def generate_auth_button(self):
        holder = tk.Frame(self.root_frame)
        holder.grid(row=4, column=0, sticky="n")
        tk.Button(holder, text="Authenticate Code", width="20", command=lambda: self.button_clicked_auth()).grid(row=0, column=0, pady=5)
        tk.Button(holder, text="Generate New Code", width="20", command=lambda: self.generate_qr_image()).grid(row=1, column=0, pady=5)

        self.generate_widget.destroy()
    
    def generate_qr_image(self):
        image = qr.QrImage("Hello world", self.qrImage)
        global_image_list["QrImage"] = image
        self.qrImage.config(image=image)

class TokenView:
    "Accepts: callback"
    # TODO: Createa a destructor to cleanup global image list

    def __init__(self, parent : tk.Frame, **kwargs):
        self.qrCode = tk.StringVar()
        self.username = tk.StringVar()
        self.root_frame = parent
        self.callback = kwargs.get("callback", None)

        self.name = "tokenview"
        current_frame = self.name

        # Configure rows' and columns' weights
        for x in range(0,5):
            parent.rowconfigure(x,weight=1)
            parent.columnconfigure(x, weight=1)

        info_frame = tk.Frame(parent)
        info_frame.grid(row=0, columnspan=5, sticky="ew")

        for x in range(0,5):
            info_frame.rowconfigure(x,weight=1)
            info_frame.columnconfigure(x, weight=1)

        tk.Button(info_frame, text="Back", command= lambda : changeView(self.root_frame, QrView)).grid(row=0, column=0, sticky="nw")
        tk.Label(info_frame, text="2FA Authentication", font=("TkDefaultFont", 18)).grid(row=0, column=1, sticky="ns")

        # Create image using PIL (required for .jpg files)
        image = Image.open("./Images/2fa.jpg")
        image = image.resize((300,200))
        image= ImageTk.PhotoImage(image)
        global_image_list["2fa"] = image

        tk.Label(parent, image=image).grid(row=1, column=0, columnspan=5)

        # Create another frame to hold the information
        loginFrame = tk.Frame(parent)
        loginFrame.grid(row=2, column=2, rowspan=5, sticky="nesw")
        
        # Setup the rows and columns in the loginFrame
        for x in range(0,5):
            loginFrame.rowconfigure(x, weight=1)
            loginFrame.columnconfigure(x, weight=1)

        tk.Label(loginFrame, text="2FA - Token", font=("TkDefaultFont", 12)).grid(column=0, row=1)

        entry = tk.Entry(loginFrame, textvariable=self.qrCode, font=("TkDefaultFont", 12))
        entry.grid(column=1, row=1)
        entry.bind("<Return>", self.button_clicked_verify)

        tk.Button(loginFrame, text="Log In", font=("TkDefaultFont", 12), command= lambda : self.button_clicked_verify(None)).grid(column=0, row=2, columnspan=2)

    def button_clicked_verify(self, event):
        str_qrcode = self.qrCode.get()
        success_or_not = verify_user_code(str_qrcode, create_one_time_password())

        if(success_or_not): #take the code inout by user, compare it to TOTP created
            print("Correct code!")
            # changeView(self.root_frame, HomeView)

class FileEncryption:
    "Accepts: home_callback, encryption_callback"
    def __init__(self, parent, **kwargs):
        self.row_count = 0
        self.name = "fileencryption"
        
        self.file = tk.StringVar()
        self.name = tk.StringVar()
        self.ext = tk.StringVar()

        for x in range(0,5):
            parent.rowconfigure(x,weight=1)
            parent.columnconfigure(x, weight=1)

        self.root = parent
        self.encrypt_callback = kwargs.get("encrypt_callback")
        self.home_callback = kwargs.get("home_callback")
        self.holder = tk.Frame(parent)
        for x in range(3):
            self.holder.rowconfigure(x,weight=1)
            self.holder.columnconfigure(x, weight=1)

        self.holder.grid(row=1, column=0,columnspan=5,sticky="news")

        self.create_title_label()
        self.create_file_path_entry()
        self.create_file_name_entry()
        self.create_file_desc_entry()
        self.create_buttons()

    def create_title_label(self):
        title_lbl = tk.Label(self.root, text='File Encryption System', font=("Helvetica", 16, "bold"), fg="#333")
        title_lbl.grid(row=0, column=0, columnspan=5, sticky="news")
    
    def create_file_path_entry(self):
        file_path_lbl = tk.Label(self.holder, text="File Path:", font=("Helvetica", 12))
        file_path_entry = tk.Entry(self.holder, textvariable=self.file, font=("Helvetica", 12), bd=2, relief="solid")
        file_path_browse = tk.Button(self.holder, text="Browse", font=("Helvetica", 12), command=lambda : browse())

        file_path_lbl.grid(row=self.row_count, column=0, sticky="e")
        file_path_entry.grid(row=self.row_count, column=1, sticky="ew")
        file_path_browse.grid(row=self.row_count, column=2, sticky="w")

        self.row_count += 1
        def browse():
            self.file.set(fs.select_file())
            self.name.set(fp.get_name(self.file.get()))
            self.ext.set(fp.get_ext(self.file.get()))

    def create_file_name_entry(self):
        file_name_lbl = tk.Label(self.holder, text="File Name:", font=("Helvetica", 12))
        file_name_entry = tk.Label(self.holder, textvariable=self.name, font=("Helvetica", 12), bd=2, relief="solid")

        file_name_lbl.grid(row=self.row_count, column=0, sticky="e")
        file_name_entry.grid(row=self.row_count, column=1, sticky="ew")

        self.row_count += 1

    def create_file_key_entry(self):
        file_key_lbl = tk.Label(self.holder, text="File Key:", font=("Helvetica", 12))
        file_key_entry = tk.Entry(self.holder, font=("Helvetica", 12), bd=2, relief="solid")

        file_key_lbl.grid(row=self.row_count, column=0)
        file_key_entry.grid(row=self.row_count, column=1)

        self.row_count += 1

    def create_file_desc_entry(self):
        file_desc_lbl = tk.Label(self.holder, text="File Type:", font=("Helvetica", 12))
        self.file_desc_entry = tk.Label(self.holder, textvariable=self.ext, font=("Helvetica", 12), bd=2, relief="solid")

        file_desc_lbl.grid(row=self.row_count, column=0, sticky="e")
        self.file_desc_entry.grid(row=self.row_count, column=1, sticky="ew")

        self.row_count += 1

    def create_buttons(self):
        btn1 = tk.Button(self.holder, text="ENCRYPT", fg="white", bg="#007BFF", font=("Helvetica", 12, "bold"), command= lambda : self.encrypt_clicked(), relief="raised", bd=2)

        btn1.grid(row=self.row_count,columnspan=5)
        self.row_count += 1

        create_directory(self.root, self.row_count)

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

def create_directory(root, row_count):
        holder = tk.Frame()
        holder.grid(row=row_count, columnspan=5, sticky="ews")

        for x in range(2):
            holder.columnconfigure(x, weight=1)

        tk.Button(holder, text="Upload/Download", fg="white", bg=f"{"#28a745" if current_frame == "" else "#28a745"}", font=("Helvetica", 12, "bold"), 
                  relief="raised", bd=2).grid(column=0, row=0, sticky="we")
        tk.Button(holder, text="Encrypt/Decrypt", fg="white", bg="#28a745", font=("Helvetica", 12, "bold"), 
                  relief="raised", bd=2, command= lambda : changeView(root, QrView)).grid(row=0, column=1, sticky="we")
        
        
        row_count += 1
