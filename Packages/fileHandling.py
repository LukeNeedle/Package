from os import path
from tkinter import filedialog

def nameCollisionHandler(fileName, extension = "txt"):
    if extension[0] == ".":
        extension = extension[1:]
    counter = 1
    newFileName = fileName
    while True:
        if path.exists(f"{newFileName}.{extension}"):
            newFileName = f"{fileName} ({counter})"
            counter += 1
        else:
            newFileName = f"{newFileName}.{extension}"
            break
    return newFileName
def nameHandler(fileName, extension = "txt"):
    return nameCollisionHandler(fileName, extension)
def name(fileName, extension = "txt"):
    return nameCollisionHandler(fileName, extension)

def pathHandler(startPosition = ".", extension = ".txt", extensionDescription = "Text File", type = "open", title = "open"):
    if extension[0] != ".":
        extension = f".{extension}"
    
    fileType = ((extensionDescription,f"*{extension}"),)
    
    fileName = ""
    while fileName == "" or fileName == "/":
        if type == "open":
            fileName = filedialog.askopenfilename(initialdir=startPosition, filetypes=fileType, title=type)
        elif type == "save":
            fileName = filedialog.asksaveasfilename(initialdir=startPosition, filetypes=fileType, defaultextension=extension, title=type)
        
        if fileName != "" and fileName != "/" and fileName != None:
            if len(fileName) < 5:
                continue
            elif fileName[-4:] != f".{extension}":
                continue
    
    return fileName

def path(startPosition = ".", extension = ".txt", extensionDescription = "Text File", type = "open"):
    return pathHandler(startPosition, extension, extensionDescription, type)