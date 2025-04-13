import os
from tkinter import Tk, filedialog

#Select a file using a GUI
def select_file(file_type):
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select file", filetypes=[("files",file_type)])  # Open file dialog to select a file
    return file_path


def select_save_as(encrypted_file_path):

    # Extract the base name of the file
    base_name = os.path.basename(encrypted_file_path)
    print("base name:", base_name)

    # If the file name ends with ".enc", remove the extension to get the original file name
    if base_name.endswith(".enc"):
        original_file_name = base_name[:-4]
    else:
        original_file_name = base_name
    print("original file name:", original_file_name)

    #Extract the original extension
    original_extension = os.path.splitext(original_file_name)[1]
    print("original extension:", original_extension)

    #GUI for save as dialog
    root = Tk()
    root.withdraw()  # Hide the root window
    save_path = filedialog.asksaveasfilename(title="Save as", defaultextension=original_extension, filetypes=[("All files", "*.*")])  # Open file dialog to select a save location
    print(save_path)  # Print the selected save path
    return save_path

if __name__ == '__main__':
    encrypted_path = select_file()
    select_save_as(encrypted_path)
