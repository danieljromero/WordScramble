# File: library.py
import glob
from pathlib import Path
# our library
library = dict()

# returns boolean from user input
def checkoption(option):
    if option.startswith("Y") or option.startswith("y"):
        return True
    else:
        return False

# returns boolean if path is a directory
def checkdir(path):
    value = Path(path)
    if value.is_dir():
        return True
    else:
        return False

# locates file(s) and returns a list
def locateall(path):
    found = glob.glob(path)
    return found

# calls start() after successfully adding a dictionary
def startover():
    prompt = input("Would you like to add more dictionaries: Y/n ")
    if checkoption(prompt):
        start()

# prompt
def dictpath():
    path = input("Enter path: ")
    return path

# gets user input and returns the correct path value
def authenticate(message, method):
    value = Path(dictpath())
    if value.is_file() and message == "file":
        print("This is a file!")
        value = str(value.resolve())
        return value
    elif value.is_dir() and (message == "directory" or message == "extension"):
        print("This is a directory!")
        value = str(value.resolve())
        return value
    else:
        print("Cannot not locate " + message + ", please try again")
        method()

# adds dictionaries to the library
def addtolibrary(list):
    for val in list:
        check = False
        while not check:
            print("For this dictionary: " + val)
            key = input("Please enter a unique key to identify it: ")
            print("Key:", key, ", Dictionary:", val)
            prompt = input("Is this information correct: Y/n ")
            if checkoption(prompt):
                library.update({key: val})
                check = True
            else:
                check = False
    print("Added to library")
    startover()

# adds single dictionary
def loadbyfile():
        value = authenticate("file", loadbyfile)
        found = locateall(value)
        addtolibrary(found)

# adds entire directory of dictionaries
def loadbydirectory():
        value = authenticate("directory", loadbydirectory)
        if value.endswith("/"):
            newpath = value + "*"
            found = locateall(newpath)
            addtolibrary(found)
        else:
            newpath = value + "/*"
            found = locateall(newpath)
            addtolibrary(found)

# adds dictionaries by extension
def loadbyextension():
        value = authenticate("extension", loadbyextension)
        extension = input("Enter file extension to use: ")
        newpath = value + "/*" + extension
        found = locateall(newpath)
        addtolibrary(found)

# single dictionary option
def single():
    option = input("Would you like to use a single dictionary: Y/n ")
    if checkoption(option):
        loadbyfile()

# multiple dictionaries option
def multiple():
    option = input("Load all dictionaries within a directory: Y/n ")
    if checkoption(option):
        loadbydirectory()

    option = input("Load specific files within a directory by extension instead: Y/n ")
    if checkoption(option):
        loadbyextension()

    if library:
        print("Current library size: " + str(len(library)))
        prompt = input("Would you like to see the value(s) in the library? Y/n ")
        if checkoption(prompt):
            print(library)
    else:
        print("Current library: empty!")

    print("Goodbye...")
    quit()

# start of application
def start():
    single()
    multiple()

start()
