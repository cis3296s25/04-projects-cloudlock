import tkinter as tk

class FileEncryption:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption System")
        self.root.geometry('500x350')
        self.root.config(bg="#f0f0f0")
        self.frame = tk.Frame(self.root, bg="#f0f0f0")
        self.frame.pack(padx=20, pady=20, expand=True)

        # Call methods to create UI elements
        self.create_title_label()
        self.create_file_path_entry()
        self.create_file_name_entry()
        self.create_file_key_entry()
        self.create_file_desc_entry()
        self.create_buttons()

    # Method Definitions
    def create_title_label(self):
        title_lbl = tk.Label(self.frame, text='File Encryption System', font=("Helvetica", 16, "bold"), fg="#333", bg="#f0f0f0")
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

    def create_file_key_entry(self):
        file_key_lbl = tk.Label(self.frame, text="File Key:", font=("Helvetica", 12), bg="#f0f0f0")
        self.file_key_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 12), bd=2, relief="solid")
        file_key_lbl.grid(row=3, column=0, pady=5, sticky="e")
        self.file_key_entry.grid(row=3, column=1, pady=5)

    def create_file_desc_entry(self):
        file_desc_lbl = tk.Label(self.frame, text="File Description:", font=("Helvetica", 12), bg="#f0f0f0")
        self.file_desc_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 12), bd=2, relief="solid")
        file_desc_lbl.grid(row=4, column=0, pady=5, sticky="e")
        self.file_desc_entry.grid(row=4, column=1, pady=5)

    def create_buttons(self):
        btn1 = tk.Button(self.frame, text="ENCRYPT", fg="white", bg="#007BFF", font=("Helvetica", 12, "bold"), command=self.encrypt_clicked, width=15, relief="raised", bd=2)
        btn2 = tk.Button(self.frame, text="HOME", fg="white", bg="#28a745", font=("Helvetica", 12, "bold"), command=self.home_clicked, width=15, relief="raised", bd=2)

        btn1.grid(row=5, column=0, columnspan=2, pady=20)
        btn2.grid(row=6, column=0, columnspan=2, pady=10)

    def encrypt_clicked(self):
        # Placeholder for encrypt logic
        print("Encrypt button clicked")

    def home_clicked(self):
        # Placeholder for home button logic
        print("Home button clicked")

# Create root window and run the application
root = tk.Tk()
app = FileEncryption(root)
root.mainloop()
