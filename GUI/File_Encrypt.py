import tkinter as tk

class FileEncryption:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption/Decryption")
        self.root.geometry('500x350')
        self.root.config(bg="#f0f0f0")
        self.frame = tk.Frame(self.root, bg="#f0f0f0")
        self.frame.pack(padx=20, pady=20, expand=True)

        # calling methods for ui elements
        self.create_title_label()
        self.create_file_path_entry()
        self.create_file_name_entry()
        self.create_file_type_entry()
        self.create_buttons()

    # defining methods
    def create_title_label(self):
        title_lbl = tk.Label(self.frame, text='File Encryption/Decryption', font=("Helvetica", 16, "bold"), fg="#333", bg="#f0f0f0")
        title_lbl.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    def create_file_path_entry(self):
        file_path_lbl = tk.Label(self.frame, text="File Path:", font=("Helvetica", 12), bg="#f0f0f0")
        self.file_path_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 12), bd=2, relief="solid")
        file_path_lbl.grid(row=1, column=0, pady=5, sticky="e")
        self.file_path_entry.grid(row=1, column=1, pady=5)

    def create_file_name_entry(self):
        file_name_lbl = tk.Label(self.frame, text="File Name:", font=("Helvetica", 12), bg="#f0f0f0")
        self.file_name_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 12), bd=2, relief="solid")
        file_name_lbl.grid(row=2, column=0, pady=5, sticky="e")
        self.file_name_entry.grid(row=2, column=1, pady=5)

    def create_file_type_entry(self):
        file_key_lbl = tk.Label(self.frame, text="File Type:", font=("Helvetica", 12), bg="#f0f0f0")
        self.file_key_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 12), bd=2, relief="solid")
        file_key_lbl.grid(row=3, column=0, pady=5, sticky="e")
        self.file_key_entry.grid(row=3, column=1, pady=5)

    def create_buttons(self):
        decrypt = tk.Button(self.frame, text="Decrypt", fg="white", bg="#007BFF", font=("Helvetica", 12, "bold"), command=self.encrypt_clicked, width=15, relief="raised", bd=2)
        loadFile = tk.Button(self.frame, text="Load File", fg="white", bg="#28a745", font=("Helvetica", 12, "bold"), command=self.loadFile_clicked, width=15, relief="raised", bd=2)
        encrypt = tk.Button(self.frame, text = "Encrypt", fg = "white", bg = "green", font=("Helvetica", 12, "bold"), command=self.encrypt_clicked, width = 15, relief = "raised", bd = 2)


        encrypt.grid(row=5, column=1, columnspan=2, pady=15)
        loadFile.grid(row=6, column=1, columnspan=2, pady=10)
        decrypt.grid(row=7, column =1, columnspan=2, pady = 15)

    # functions for encrypt, decrypt, and home button
    def encrypt_clicked(self):
        print("Encrypt button clicked")

    def loadFile_clicked(self):
        print("Load File button clicked")

    def decrypt_clicked(self):
        print("Decrpyt button clicked")

# creating the root application and running
root = tk.Tk()
app = FileEncryption(root)
root.mainloop()
