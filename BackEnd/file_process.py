import os 

def get_name(path : str):
    head, tail = os.path.split(path)
    return tail

def get_ext(path : str):
    filename, extension = os.path.splitext(path)
    return extension
