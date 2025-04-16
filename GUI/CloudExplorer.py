from math import exp
import string
from tkinter import BOTH, END, LEFT, N, RIGHT, YES, Button, Entry, Label, Listbox, Scrollbar, StringVar, filedialog, Toplevel
from tkinter import Tk, Frame, BOTTOM, TOP, X, Y
from tkinter.simpledialog import _setup_dialog

from typing import List, Self



class File:
    '''Class that contains information about a file'''
    def __init__(self, name:string):
        self.name = name

class Directory:
    '''Class that contains information about a directory'''
    def __init__(self, name:string, directoryList : List[Self] = None,
                  fileList:List[File]=None):
        self.name = name
        self.files = fileList
        self.dirs = directoryList

class CurrentEnv:
    '''Class that contains a list of files and directories, as well as a reference to the previous enviroment'''
    def __init__(self, name:string = None, dirList:List[Directory] = None, 
                 fileList:List[File]=None, prev:Self = None):
        self.name = name
        self.dirList = dirList
        self.fileList = fileList
        self.prev = prev

class CloudExplorer:
    def __init__(self, master, currentEnv : CurrentEnv, title="Default"):
        self.master = master
        self.top = Toplevel(master)
        self.top.title(title)
        self.top.iconname(title)
        self.top.geometry("340x340")
        self.currentEnv = currentEnv
        _setup_dialog(self.top) # Sets platform specific attributes

        self.currentIndex = 0
        self.selectedvar = StringVar(self.top)
        self.dirvar = StringVar(self.top, value="/")

        self.topframe = Frame(self.top)
        self.topframe.pack(side=TOP, fill=X, expand=False)

        self.midframe = Frame(self.top)
        self.midframe.pack(fill=BOTH, expand=True)

        self.botframe = Frame(self.top, bg="red")
        self.botframe.pack(side=BOTTOM, fill=BOTH, expand=False)

        # Setup current dir/file
        self.dirdisplay = Entry(self.topframe, textvariable=self.dirvar, state="readonly")
        self.dirdisplay.pack(fill=X, expand=False)

        # Setup file selection
        self.filebar = Scrollbar(self.midframe)
        self.filebar.pack(side=RIGHT, fill=Y)
        self.filelist = Listbox(self.midframe, yscrollcommand=(self.filebar, "set"))
        self.filelist.pack(side=LEFT, fill=BOTH, expand=True)

        self.filebar.config(command=(self.filelist, 'yview'))

        # Setup holder to hold 3 components
        self.holder = Frame(self.botframe)
        self.holder.pack(fill=X, expand=True)

        self.backbutton = Button(self.holder, text="Back", command=self.Back)
        self.backbutton.pack(side=LEFT, expand=False)

        self.confirmbutton = Button(self.holder, text="Confirm", command = self.Confirm_Event)
        self.confirmbutton.pack(side=RIGHT, expand=False)

        self.selectionentry = Entry(self.holder, textvariable=self.selectedvar, state="readonly")
        self.selectionentry.pack(fill=X, expand=True)



        #Setup selected file view
        self.filelist.bind('<<ListboxSelect>>', self.Single_Click_Event)
        self.filelist.bind('<Double-ButtonRelease-1>', self.Double_Click_Event, add="+")
        self.filelist.bind('<Return>', self.Confirm_Event, add="+")

        self.Get_Files()

    def Get_Files(self, newEnv : CurrentEnv= None):
        '''
        If given a new newEnv, will render that enviroment
        
        Otherwise, will render the enviroment provided by default
        '''
        self.dir_end = -1
        self.filelist.delete(0, END)
        self.selectedvar.set("")

        if newEnv is not None:
            if newEnv == self.currentEnv.prev:
                # We are going back
                self.currentEnv = newEnv
                self.currentIndex = 0
                self.dirvar.set(self.currentEnv.name)
            else:
                # We are still getting a new enviroment
                newEnv.prev = self.currentEnv
                self.currentEnv = newEnv
                self.dirvar.set(self.currentEnv.name)
        else:
            # Rendering default
            self.currentEnv.name = "/"

            
        if self.currentEnv.dirList:
            for dir in self.currentEnv.dirList:
                self.filelist.insert(END, "DIRECTORY: " + dir.name)
                self.dir_end += 1
        if self.currentEnv.fileList:
            for file in self.currentEnv.fileList:
                self.filelist.insert(END, "FILE: " + file.name)

        self.selectedvar.set(self.Get_Reference(self.currentIndex))

    def Single_Click_Event(self, event):
        w = event.widget # Get the Listbox Reference
        if w.curselection():
            self.currentIndex = int(w.curselection()[0]) # Select the item
            self.selectedvar.set(self.Get_Reference(self.currentIndex))
        #TODO: handle empty lists

    def Double_Click_Event(self, event):
        if (self.currentIndex > self.dir_end):
            # File was selected
            self.Confirm_Event()
        else:
            # Directory was selected
            directory = self.currentEnv.dirList[self.currentIndex]
            ce = CurrentEnv(name = self.currentEnv.name +directory.name + "/", 
                            dirList=directory.dirs, 
                            fileList=directory.files)
            self.Get_Files(ce)

    def Confirm_Event(self, event=None):
        selected = self.dirvar.get()+self.selectedvar.get()
        print(selected)
        
    def Back(self):
        self.Get_Files(self.currentEnv.prev)
        pass
    
    def Get_Reference(self, index):
        ref = ""
        if self.currentEnv.dirList:
            if index < len(self.currentEnv.dirList):
                ref = self.currentEnv.dirList[index].name
                print(ref)
                return ref
        if self.currentEnv.fileList:
            ref = self.currentEnv.fileList[index-self.dir_end-1].name
            print(ref)
            return ref
        return ref

        # Download the selected file/dir

    

if __name__ == "__main__":
    files = [File("1"), File("2"), File("3"), File("1"), File("2"), File("3"), File("1"), File("2"), File("3"), File("1"), File("2"), File("3"), File("1"), File("2"), File("3"), File("1"), File("2"), File("3"), File("1"), File("2"), File("3"), File("1"), File("2"), File("3"), File("1"), File("2"), File("3"), ]
    files2 = [File("4"), File("5"), File("6")]
    dir2 = [Directory("hello")]
    dir = [Directory("Dir", directoryList=dir2,fileList=files2)]

    ce = CurrentEnv(name="/")

    # for thing in ce.dirList:
    #     print(thing.name)
    # for thing in ce.fileList:
    #     print(thing.name)

    root = Tk()
    CloudExplorer(root, ce)
    root.mainloop()