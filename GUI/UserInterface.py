"Collection of classes to display user interface"
from email import message
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import PIL.Image
from BackEnd.Microsoft_Auth import *
from BackEnd.hybrid_crypto import *
from BackEnd.Cloud_Connect import *
import BackEnd.file_search as fs
import BackEnd.file_process as fp
import BackEnd.Generate_Qr as qr

global_image_list = {} # global image object to avoid the garbage collection
current_name = None
global_username = ""
global_secret_key = ""

def changeView(root : tk.Frame, view):
    for child in root.winfo_children():
        child.destroy()
    view(root)

class QrView:
    """Accepts: callback"""
    # TODO: Createa a destructor to cleanup global image list
    def __init__(self, parent : tk.Frame):
        self.name = "qrview"
        current_name = self.name # Set the current frame name to qrview
        self.root = parent
        if(global_username):
            username = global_username
        else:
            username = ""
        self.username = StringVar(self.root, username)

        # Configure rows' weights
        for x in range(9):
            self.root.rowconfigure(x,weight=1, uniform="row")
            self.root.columnconfigure(x,weight=1)

        # Add the elements to prompt the user to scan the generated QR image
        tk.Label(parent, text="2FA GENERATION", font=("TkDefaultFont", 18)).grid(row=0,column=0, columnspan=10, sticky="news")

        self.qrImage = tk.Label(self.root)
        self.qrImage.grid(row=1, column=0, rowspan=4, columnspan=10, sticky="news")

        tk.Label(parent, text="Microsoft Authentication Username", font=("TkDefaultFont", 12)).grid(row=5,column=0, columnspan=10, sticky="news")
        tk.Entry(parent, textvariable=self.username, font=("TkDefaultFont", 12)).grid(row=6, column=0, columnspan=10, sticky="n")

        self.generate_widget = tk.Button(parent, text="Generate QR", width="20", command=lambda: self.Generate_Event())
        self.generate_widget.grid(row=7, columnspan=10, sticky="n")

        # If we already have a stored image, load it back
        if "QrImage" in global_image_list:
            print("QrCode already exists!!!")
            self.qrImage.configure(image=global_image_list["QrImage"])
            self.qrImage.image = global_image_list["QrImage"]
            self.Auth_Create()
        else:
            print("QrCode does not exist!!!")

    def Generate_Event(self):
        global global_username, global_secret_key
        
        # Get username from text box
        username = self.username.get()
        
        # Check if username is empty and print error if it is
        if not username:
            print("Username cannot be empty")
            messagebox.showerror(self.root, message="Username cannot be empty")
            return
        
        # Set the global username and retrieve the secret key for this user
        global_username = username
        global_secret_key = get_secret_key(global_username)
        self.link = authenticate_acct(global_username, global_secret_key)
        self.Generate_Image()
        
        # Create authentication buttons
        self.Auth_Create()

    def Auth_Event(self):
        changeView(self.root, TokenView)

    def Auth_Create(self):
        self.generate_widget.destroy()
        tk.Button(self.root, text="Authenticate Code", width="20", command=lambda: self.Auth_Event()).grid(row=7, column=0, columnspan=10, sticky="n")

    def Generate_Image(self):
        self.image = qr.QrImage(self.link, self.qrImage)
        global_image_list["QrImage"] = self.image
        self.qrImage.config(image=self.image)

class TokenView:
    "Accepts: callback"
    def __init__(self, parent : tk.Frame, **kwargs):
        self.qrCode = tk.StringVar()
        self.username = tk.StringVar()
        self.root_frame = parent
        self.callback = kwargs.get("callback", None)

        self.name = "tokenview"
        current_name = self.name

        # Configure rows' and columns' weights
        for x in range(10):
            parent.rowconfigure(x,weight=1)
            parent.columnconfigure(x, weight=1)

        info_frame = tk.Frame(parent)
        info_frame.grid(row=0, columnspan=10, sticky="ew")

        for x in range(5):
            info_frame.rowconfigure(x,weight=1)
            info_frame.columnconfigure(x, weight=1)

        tk.Button(info_frame, text="Back", command= lambda : changeView(self.root_frame, QrView)).grid(row=0, column=0, sticky="nw")
        tk.Label(info_frame, text="2FA Authentication", font=("TkDefaultFont", 18)).grid(row=0, column=1, columnspan=2,sticky="ns")


        # Create image using PIL (required for .jpg files)
        self.image = PIL.Image.open("./Images/2fa.jpg")
        self.image = self.image.resize((300,200))
        self.image= ImageTk.PhotoImage(self.image)
        global_image_list["2fa"] = self.image

        tk.Label(parent, image=self.image).grid(row=1, rowspan=4,column=0, columnspan=10, sticky="news")

        # Create another frame to hold the information
        loginFrame = tk.Frame(parent)
        loginFrame.grid(row=5, column=4, rowspan=10, sticky="news")
        
        # Setup the rows and columns in the loginFrame
        for x in range(2):
            loginFrame.rowconfigure(x, weight=1)
            loginFrame.columnconfigure(x, weight=1)

        tk.Label(loginFrame, text="2FA - Token", font=("TkDefaultFont", 12)).grid(column=0, row=0)
        tk.Entry(loginFrame, textvariable=self.qrCode, font=("TkDefaultFont", 12)).grid(column=1, row=0)
        # entry.bind("<Return>", self.button_clicked_verify)

        tk.Button(parent, text="Log In", font=("TkDefaultFont", 12), command= lambda : self.button_clicked_verify(None)).grid(column=4, row=8, columnspan=2)

    def button_clicked_verify(self, event):
        str_qrcode = self.qrCode.get()
        one_time_code = create_one_time_password(global_secret_key)
        success_or_not = verify_user_code(str_qrcode, one_time_code)

        if(success_or_not): #take the code inout by user, compare it to TOTP created
            print("Correct code!")
            changeView(self.root_frame, FileEncryption)
        else:
            messagebox.showerror(self.root_frame, message="Invalid code!")

    def __del__(self):
        del self.image

class FileEncryption:
    def __init__(self, parent):
        self.row_count = 0
        self.name = "fileencryption"
        
        self.file = tk.StringVar()
        self.name = tk.StringVar()
        self.ext = tk.StringVar()

        for x in range(10):
            parent.rowconfigure(x,weight=1)
            parent.columnconfigure(x, weight=1)

        self.root = parent
        self.holder = tk.Frame(parent)
        self.holder.rowconfigure((0,1,2,3,4,5), weight=1)
        self.holder.columnconfigure((0,1,2), weight=1)

        self.holder.grid(row=1, column=0, rowspan=6,columnspan=10,sticky="news")

        self.create_title_label()
        self.create_file_path_entry()
        self.create_file_name_entry()
        self.create_file_desc_entry()
        self.create_buttons()

    def create_title_label(self):
        title_lbl = tk.Label(self.root, text='File Encryption System', font=("Helvetica", 16, "bold"), fg="#333")
        title_lbl.grid(row=0, column=0, columnspan=10, sticky="news")
    
    def create_file_path_entry(self):
        file_path_lbl = tk.Label(self.holder, text="File Path:", font=("Helvetica", 12))
        file_path_entry = tk.Entry(self.holder, textvariable=self.file, font=("Helvetica", 12), bd=2, relief="solid")
        file_path_browse = tk.Button(self.holder, text="Browse", font=("Helvetica", 12), command=lambda : browse())

        file_path_lbl.grid(row=0, rowspan=2,column=0, sticky="e")
        file_path_entry.grid(row=0, rowspan=2,column=1, sticky="ew")
        file_path_browse.grid(row=0, rowspan=2,column=2, sticky="w")

        def browse():
            self.file.set(fs.select_file(".*"))
            self.name.set(fp.get_name(self.file.get()))
            self.ext.set(fp.get_ext(self.file.get()))

    def create_file_name_entry(self):
        file_name_lbl = tk.Label(self.holder, text="File Name:", font=("Helvetica", 12))
        file_name_entry = tk.Label(self.holder, textvariable=self.name, font=("Helvetica", 12), bd=2, relief="solid")

        file_name_lbl.grid(row=2, rowspan=2,column=0, sticky="e")
        file_name_entry.grid(row=2, rowspan=2,column=1, sticky="ew")

    def create_file_key_entry(self):
        file_key_lbl = tk.Label(self.holder, text="File Key:", font=("Helvetica", 12))
        file_key_entry = tk.Entry(self.holder, font=("Helvetica", 12), bd=2, relief="solid")

        file_key_lbl.grid(row=4, rowspan=2,column=0)
        file_key_entry.grid(row=4, rowspan=2,column=1)

    def create_file_desc_entry(self):
        file_desc_lbl = tk.Label(self.holder, text="File Type:", font=("Helvetica", 12))
        self.file_desc_entry = tk.Label(self.holder, textvariable=self.ext, font=("Helvetica", 12), bd=2, relief="solid")

        file_desc_lbl.grid(row=6, rowspan=2,column=0, sticky="e")
        self.file_desc_entry.grid(row=6, rowspan=2,column=1, sticky="ew")


    def create_buttons(self):
        buttonholder = tk.Frame(self.root)
        buttonholder.grid(row=8,columnspan=10)
        buttonholder.columnconfigure(0, weight=1)
        buttonholder.columnconfigure(1, weight=1)
    
        btn1 = tk.Button(buttonholder, text="ENCRYPT", fg="white", bg="#007BFF", font=("Helvetica", 12, "bold"), command= lambda : self.encrypt_clicked(), relief="raised")
        btn2 = tk.Button(buttonholder, text="DECRYPT", fg="white", bg="#007BFF", font=("Helvetica", 12, "bold"), command= lambda : self.decrypt_clicked(), relief="raised")

        btn1.grid(row=0, column=0)
        btn2.grid(row=0, column=1)
        self.row_count += 1

        create_directory(self.root)

    def success_window(self,encrypt_or_decrypt):
        # TODO: hybrid_encrypt() and decrypt() return Boolean for success
        top = Toplevel(self.root)
        top.geometry("500x200")
        top.title("Success")
        time_taken = aes_time()
        Label(top, text=("Time taken: " + time_taken), font=("Tk Default Font", 12)).place(x=150, y=50)
        Label(top, text=("File " + encrypt_or_decrypt + ": " + self.name.get()), font=("Tk Default Font", 12)).place(x=150, y=100)

    def encrypt_clicked(self):
        #get the file path from the entry
        file_path = self.file.get()

        #check if the file path is empty
        if not file_path:
            print("No file selected.")
            return

        #call hybrid_encrypt method
        if hybrid_encrypt(file_path):
            print("Successfully encrypted")
            self.success_window("encrypted")

        print("Encrypted file saved to: ", file_path)

    def decrypt_clicked(self):
        #get the file path from the entry
        file_path = self.file.get()

        #check if the file path is empty
        if not file_path:
            print("No file selected.")
            return
        
        #select the save as a file path
        save_path = fs.select_save_as(file_path)

        #check if the save path is empty
        if not save_path:
            print("No save path selected.")
            return

        #call hybrid_decrypt method
        if hybrid_decrypt(file_path, save_path):
            print("Successfully decrypted")
            self.success_window("decrypted")

        print("Decrypt button clicked")

    def home_clicked(self, **kwargs):
        if self.home_callback != None:
            self.callback()
        # Placeholder for home button logic
        print("Home button clicked")

def create_directory(root):
        holder = tk.Frame(root)
        holder.grid(row=10, column=0,columnspan=10, sticky="news")

        for x in range(2):
            holder.columnconfigure(x, weight=1)

        tk.Button(holder, text="Encrypt/Decrypt", fg="white", bg=f"{"#28a745" if current_name == "" else "#28a745"}", font=("Helvetica", 12, "bold"),
                  relief="raised", command= lambda : changeView(root, FileEncryption), width=5).grid(row=0, column=0,sticky="news")
        tk.Button(holder, text="Cloud", fg="white", bg="#28a745", font=("Helvetica", 12, "bold"),
                  relief="raised", command= lambda : changeView(root, Cloud), width=5).grid(row=0, column=1,sticky="news")

class Cloud:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="#f7f7f7")  #a lighter background
        
        self.file = tk.StringVar()
        self.name = tk.StringVar()
        self.ext = tk.StringVar()

        self.bucket = tk.StringVar()
        self.accessKey = tk.StringVar()
        self.secretKey = tk.StringVar()

        for x in range(10):
            self.root.rowconfigure(x, weight=1)
            self.root.columnconfigure(x, weight=1)

        title_lbl = tk.Label(self.root, text='File Cloud Upload', font=("Helvetica", 16, "bold"), fg="black", bg="#f7f7f7")
        title_lbl.grid(row=0, column=0, columnspan=8, sticky="news")

        s3_bucket_lbl = tk.Label(self.root, text="S3 Bucket Name:", font=("Helvetica", 12), bg="#f7f7f7")
        s3_bucket_lbl.grid(row=1, column=0, sticky="e")
        
        self.s3_bucket_entry = ttk.Entry(self.root, textvariable=self.bucket, font=("Helvetica", 12))
        self.s3_bucket_entry.grid(row=1, column=1, sticky="ew")

        access_key_lbl = tk.Label(self.root, text="Access Key:", font=("Helvetica", 12), bg="#f7f7f7")
        access_key_lbl.grid(row=2, column=0, sticky="e")

        self.access_key_entry = ttk.Entry(self.root, textvariable=self.accessKey, font=("Helvetica", 12))
        self.access_key_entry.grid(row=2, column=1, sticky="ew")

        secret_key_lbl = tk.Label(self.root, text="Secret Key:", font=("Helvetica", 12), bg="#f7f7f7")
        secret_key_lbl.grid(row=3, column=0, sticky="e")

        self.secret_key_entry = ttk.Entry(self.root, textvariable=self.secretKey, font=("Helvetica", 12))
        self.secret_key_entry.grid(row=3, column=1, sticky="ew")
        
        file_path_lbl = tk.Label(self.root, text="File Path:", font=("Helvetica", 12), bg="#f7f7f7")
        file_path_lbl.grid(row=4, column=0, sticky="e")

        self.file_path_entry = ttk.Entry(self.root, textvariable=self.file, font=("Helvetica", 12), state="readonly")
        self.file_path_entry.grid(row=4, column=1, sticky="ew")

        browseFile = tk.Button(self.root, text="Browse", command=self.browseFile_clicked)
        browseFile.grid(row=4,column=2, sticky="w")

        file_name_lbl = tk.Label(self.root, text="File Name:", font=("Helvetica", 12), bg="#f7f7f7")
        file_name_lbl.grid(row=5, column=0, sticky="e")

        self.file_name_entry = ttk.Entry(self.root, textvariable=self.name, font=("Helvetica", 12), state="readonly")
        self.file_name_entry.grid(row=5, column=1, sticky="ew")

        file_type_lbl = tk.Label(self.root, text="File Type:", font=("Helvetica", 12), bg="#f7f7f7")
        file_type_lbl.grid(row=6, column=0, sticky="e")

        self.file_type_entry = ttk.Entry(self.root, textvariable=self.ext, font=("Helvetica", 12), state="readonly")
        self.file_type_entry.grid(row=6, column=1, sticky="ew")

        
        # styling for buttons
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12, "bold"))
        style.configure("TButton", relief="flat")  # Flat button for modern look

        self.holder = tk.Frame(self.root)
        self.holder.grid(row=7, columnspan=8, sticky="s")
        for x in range(3):
            self.holder.columnconfigure(x, weight=1)

        upload = tk.Button(self.holder, text="Upload", fg="white", bg="#007BFF" , font=("Helvetica", 12, "bold"), command=self.upload_clicked)
        upload.grid(row=0,column=1)

        create_directory(self.root)

    # button click functions
    def browseFile_clicked(self):
        self.file.set(fs.select_file(".*"))
        self.name.set(fp.get_name(self.file.get()))
        self.ext.set(fp.get_ext(self.file.get()))

    def upload_clicked(self):
        bucket = self.bucket.get()
        accessKey = self.accessKey.get()
        secretKey = self.secretKey.get()
        filePath = self.file.get()

        setAws(bucket, accessKey, secretKey)
        
        if not filePath:
            print("No file selected.")
            return
        
        rawFilePath = r"{}".format(filePath)
        fileKey = self.name.get()
        if uploadS3(rawFilePath, fileKey):
            print("Successfully uploaded", fileKey)

