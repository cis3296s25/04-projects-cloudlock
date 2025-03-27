import tkinter as tk
from tkinter import Label, Button, Entry

# creating root window
root = tk.Tk()

#title and dimensions
root.title("File Encryption System")
root.geometry('500x350')  # adjusted to a slightly larger size for a balanced layout

# neutral backround
root.config(bg="#f0f0f0")

# creating a frame to contain all elements
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=20, pady=20, expand=True)

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

# execute
root.mainloop()
