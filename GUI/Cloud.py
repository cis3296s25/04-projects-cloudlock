import tkinter as tk
from tkinter import ttk

class Cloud:
    def __init__(self, root):
        self.root = root
        self.root.title("Cloud")
        self.root.geometry('500x350')
        self.root.config(bg="#f7f7f7")  #a lighter background
        self.frame = tk.Frame(self.root, bg="#f7f7f7")
        self.frame.pack(padx=20, pady=20, expand=True)

        # calling methods
        self.title_label()
        self.s3_bucket()
        self.access_key()
        self.secret_key()
        self.file_path()
        self.file_name()
        self.file_type()
        self.create_buttons()

    def title_label(self):
        title_lbl = tk.Label(self.frame, text='File Cloud Upload', font=("Segoe UI", 22), fg="black", bg="#f7f7f7")
        title_lbl.grid(row=0, column=1, columnspan=1, pady=(0, 20))

    def s3_bucket(self):
        s3_bucket_lbl = tk.Label(self.frame, text="S3 Bucket Name:", font=("Segoe UI", 12), bg="#f7f7f7")
        self.s3_bucket_entry = ttk.Entry(self.frame, font=("Segoe UI", 12), width=40)
        s3_bucket_lbl.grid(row=1, column=0, pady=5, sticky="e")
        self.s3_bucket_entry.grid(row=1, column=1, pady=5)

    def access_key(self):
        access_key_lbl = tk.Label(self.frame, text="Access Key:", font=("Segoe UI", 12), bg="#f7f7f7")
        self.access_key_entry = ttk.Entry(self.frame, font=("Segoe UI", 12), width=40)
        access_key_lbl.grid(row=2, column=0, pady=5, sticky="e")
        self.access_key_entry.grid(row=2, column=1, pady=5)

    def secret_key(self):
        secret_key_lbl = tk.Label(self.frame, text="Secret Key:", font=("Segoe UI", 12), bg="#f7f7f7")
        self.secret_key_entry = ttk.Entry(self.frame, font=("Segoe UI", 12), width=40)
        secret_key_lbl.grid(row=3, column=0, pady=5, sticky="e")
        self.secret_key_entry.grid(row=3, column=1, pady=5)

    def file_path(self):
        file_path_lbl = tk.Label(self.frame, text="File Path:", font=("Segoe UI", 12), bg="#f7f7f7")
        self.file_path_entry = ttk.Entry(self.frame, font=("Segoe UI", 12), width= 40)
        file_path_lbl.grid(row=4, column=0, pady=5, sticky="e")
        self.file_path_entry.grid(row=4, column=1, pady=5)

    def file_name(self):
        file_name_lbl = tk.Label(self.frame, text="File Name:", font=("Segoe UI", 12), bg="#f7f7f7")
        self.file_name_entry = ttk.Entry(self.frame, font=("Segoe UI", 12), width=40)
        file_name_lbl.grid(row=5, column=0, pady=5, sticky="e")
        self.file_name_entry.grid(row=5, column=1, pady=5)

    def file_type(self):
        file_type_lbl = tk.Label(self.frame, text="File Type:", font=("Segoe UI", 12), bg="#f7f7f7")
        self.file_type_entry = ttk.Entry(self.frame, font=("Segoe UI", 12), width=40)
        file_type_lbl.grid(row=6, column=0, pady=5, sticky="e")
        self.file_type_entry.grid(row=6, column=1, pady=5)

    # creating buttons
    def create_buttons(self):
        # ttk buttons for a sleeker design
        loadFile = ttk.Button(self.frame, text="Load File", style="TButton", command=self.loadFile_clicked)
        download = ttk.Button(self.frame, text="Download", style="TButton", command=self.download_clicked)
        upload = ttk.Button(self.frame, text="Upload", style="TButton", command=self.upload_clicked)

        # styling for buttons
        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 12, "bold"), width=15, padding=6)
        style.configure("TButton", relief="flat")  # Flat button for modern look
        
        loadFile.grid(row=7, column=0, pady=10, padx=5)
        download.grid(row=7, column=1, pady=10, padx=5)
        upload.grid(row=7, column=2, pady=10, padx=5)

    # button click functions
    def loadFile_clicked(self):
        print("Load File button clicked")

    def download_clicked(self):
        print("Download button clicked")

    def upload_clicked(self):
        print("Upload button clicked")

root = tk.Tk()
app = Cloud(root)
root.mainloop()
