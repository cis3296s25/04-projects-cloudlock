from tkinter import Tk, filedialog


def select_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select file", filetypes=[("files", "*.txt")])
    return file_path


if __name__ == '__main__':
    select_file()
