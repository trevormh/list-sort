import FileSort
from Tkinter import *
import re
import os

#gets the current item that was clicked in the window
def GetWindowIndex(self, event):
    w = event.widget
    self.curIndex = int(w.curselection()[0])

#moves the current item in the window when clicked/dragged in listbox2 
def MoveWindowItem(self, event):
    i = self.listbox2.nearest(event.y)
    if i < self.curIndex:
        x = self.listbox2.get(i)
        self.listbox2.delete(i)
        self.listbox2.insert(i+1, x)
        self.curIndex = i
    elif i > self.curIndex:
        x = self.listbox2.get(i)
        self.listbox2.delete(i)
        self.listbox2.insert(i-1, x)
        self.curIndex = i
    RenumberList(self) #now renumber the list because we just changed the numberical order of the listing

#re-numbers the list so everything is in ascending order
def RenumberList(self):
    tempFiles = []
    i = 1
    for filename in self.listbox2.get(0, END):
        newfilename = re.sub(r'^[0-9]*[.]',"",filename)
        tempFiles.insert(i, str(i).rjust(2,'0') + "." + newfilename)
        i = i + 1
        
    i = 0
    for filename in tempFiles:
        self.listbox2.delete(i,i)
        self.listbox2.insert(i, filename)
        i = i + 1

#save the playlist order by re-writing filenames with appended number    
def SaveList(self, directory):
    templist = []
    templistbox2 = []
    for n,i in enumerate(self.listbox2.get(0,END)): #create a temporary list of the items in listbox 2
       templistbox2.insert(n, re.sub(r'^[0-9]*[.]',"",str(i)).lstrip())  #remove the leading numbers
    for name in sorted(os.listdir(directory)):  #loop through the directory of files which we're modifying
        filename = re.sub(r'^[0-9.]+', '', name).lstrip()  #remove any numbers they may have
        if(filename in templistbox2):  #check to see if the current file is in this directory
            num = templistbox2.index(filename) + 1  #if, find it's index number in listbox2
            if(num < 10):
                num = str(num).rjust(2,'0') #if the number is less than 10, add leading zero's
            os.rename(directory + "/" + name, directory + "/" + str(num + ". " + filename))  #now rename the file

#takes the selected item from the directory and adds it tot he new list    
def AddToListTwo(self,IndexPosition):
  filename = RemoveLeadingNums(self, str(self.listbox1.get(IndexPosition))) #get the filename, remove the leading numbers if there are any
	List2Contents = RemoveLeadingNums(self, self.listbox2.get(0, END))
	if(type(List2Contents) == NoneType):
	    self.listbox2.insert(0, filename)
	else:
	    if(filename not in List2Contents): #make sure the file isn't already in list 2
	        self.listbox2.insert(0, filename)
	RenumberList(self)
	
#adds all files from the directory to list2 instead of individually adding them
def AddAllFiles(self):
	i = 0
	List2Contents = RemoveLeadingNums(self, self.listbox2.get(0, END))
	for filename in self.listbox1.get(0, END):
	    newfilename = RemoveLeadingNums(self,str(filename))
	    if(newfilename not in List2Contents): #make sure the file isn't already in list 2
	        self.listbox2.insert(END, newfilename)
	        pass
	RenumberList(self)

def RemoveFromListTwo(self, IndexPosition):
	filename = self.listbox2.get(IndexPosition) #get the filename
	List2Contents = self.listbox2.get(0, END)
	if(filename in List2Contents): #make sure the file isn't already in list 2
		self.listbox2.delete(IndexPosition)
	RenumberList(self)

def RemoveLeadingNums(self, words):
    if(isinstance(words,str)):
        return re.sub(r'^[0-9.]+', '', words.lstrip())
    else:
        i = 0
        returnlist = []
        for word in words:
           newword = re.sub(r'^[0-9.]+', '', word.lstrip())
           returnlist.insert(0,newword)
           i += 1
        return returnlist
	
