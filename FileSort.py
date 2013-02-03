from Tkinter import *
import Tkinter
import SortActions
import tkFileDialog
import os

class MakeList(Tkinter.Listbox):
    
    def __init__(self,root):
        self.BuildMainWindow(root)
        self.ListboxSet = 0 
        return
    
    #displays the menu bar and options
    def BuildMainWindow(self, root):
        menubar = Menu(root)
        root.config(menu=menubar)
        
        # Create a menu button labeled "File" that brings up a menu
        filemenu = Menu(menubar)
        menubar.add_cascade(label='File', menu=filemenu)
        
        # Create entries in the "File" menu
        # simulated command functions that we want to invoke from our menus
        filemenu.add_command(label='Open', command=self.openfile)
        filemenu.add_separator(  )
        filemenu.add_command(label='Quit', command=sys.exit)
    
    #upon selecting a directory from the menu and listboxes/buttons are created
    def BuildListbox(self, directory):
        self.scrollbar1 = Tkinter.Scrollbar(orient = VERTICAL)
        self.listbox1 = Tkinter.Listbox( width=50, height = 30, yscrollcommand=self.scrollbar1.set)
        self.scrollbar2 = Tkinter.Scrollbar(orient = VERTICAL)
        self.listbox2 = Tkinter.Listbox(width = 50, height = 30, yscrollcommand=self.scrollbar2.set)
        
        self.listbox1.grid(row=1, column=0, rowspan = 4, columnspan = 5)
        self.scrollbar1.grid(row = 0, column = 5, rowspan = 5)
        self.scrollbar1["command"]=self.listbox1.yview

        self.listbox2.grid(row=1 ,column=15, rowspan = 4, columnspan = 5)
        self.scrollbar2.grid(row = 0, column = 20, rowspan = 5)
        self.scrollbar2["command"]=self.listbox2.yview
        self.listbox2.bind('<<ListboxSelect>>', lambda e:SortActions.GetWindowIndex(self,e))
        self.listbox2.bind('<B1-Motion>', lambda e:SortActions.MoveWindowItem(self,e))
    
        i = 0
        for filename in sorted(os.listdir(directory)):
            self.listbox1.insert(i, filename)
            i = i + 1
    
        self.bAddToListTwo = Button(text = "->", command = lambda:SortActions.AddToListTwo(self,self.listbox1.curselection()))
        self.bAddToListTwo.grid(row=1, column = 6)
        self.bAddAll = Button(text = "Add All To Playlist", command = lambda:SortActions.AddAllFiles(self))
        self.bAddAll.grid(row=2, column = 6)
        self.bRemoveFromListTwo = Button(text = "Remove From Playlist", command = lambda:SortActions.RemoveFromListTwo(self,self.listbox2.curselection()))
        self.bRemoveFromListTwo.grid(row=3, column = 6)
        self.bSavePlaylist = Button(text = "Save Playlist", command = lambda:SortActions.SaveList(self, directory))
        self.bSavePlaylist.grid(row=4, column = 6)
    
    def openfile(self): #select a directory to view files
        if(self.ListboxSet == 1): #empty the list and remove the buttons from the frame
            self.listbox1.forget()
            self.listbox2.forget()
            self.bAddToListTwo.forget()
            self.bRemoveFromListTwo.forget()
            self.bAddAll.forget()
            self.bSavePlaylist.forget()
        directory = tkFileDialog.askdirectory(initialdir='.')
        self.BuildListbox(directory)
        self.ListboxSet = 1
        return
    
    

if __name__ == '__main__':
    root = Tk()
    start = MakeList(root)
    mainloop()
