# File: library.py
import glob
import json
from pathlib import Path

# our path library
pathlibrary = dict()


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


# calls start() after successfully adding a path to path library
def startover():
    prompt = input("Would you like to add more paths to library: Y/n ")
    if checkoption(prompt):
        start()
    else:
        print("continuing...")
        openallpaths(pathlibrary)


# prompt
def dictpath():
    path = input("Enter path: ")
    return path


def printlibrary(lib):
    for k, v in lib.items():
        print("Key: ["+ k +"] " + "Path: [" + v + "]")


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


# adds dictionaries to the path library
def addtolibrary(list):
    for val in list:
        check = False
        while not check:
            print("For this path: " + val)
            key = input("Please enter a unique key to identify it: ")
            print("Key:", key, ", Path:", val)
            prompt = input("Is this information correct: Y/n ")
            if checkoption(prompt):
                pathlibrary.update({key: val})
                check = True
            else:
                check = False
    print("Added!")
    startover()


# adds path to a single dictionary to path library
def usebyfile():
    value = authenticate("file", usebyfile)
    found = locateall(value)
    addtolibrary(found)


# adds path to an entire directory of dictionaries to path library
def usebydirectory():
    value = authenticate("directory", usebydirectory)
    if value.endswith("/"):
        newpath = value + "*"
        found = locateall(newpath)
        addtolibrary(found)
    else:
        newpath = value + "/*"
        found = locateall(newpath)
        addtolibrary(found)


# adds paths of dictionaries by extension to path library
def usebyextension():
    value = authenticate("extension", usebyextension)
    extension = input("Enter file extension to use: ")
    newpath = value + "/*" + extension
    found = locateall(newpath)
    addtolibrary(found)


# single dictionary option
def single():
    option = input("Add a single dictionary to new path library: Y/n ")
    if checkoption(option):
        usebyfile()


# multiple dictionaries option
def multiple():
    option = input("Add entire directory of dictionaries to new path library: Y/n ")
    if checkoption(option):
        usebydirectory()

    option = input("Add dictionaries by extension to new path library: Y/n ")
    if checkoption(option):
        usebyextension()

    if pathlibrary:
        print("Current path library size: " + str(len(pathlibrary)))
        prompt = input("Would you like to see the value(s) in the path library? Y/n ")
        if checkoption(prompt):
            printlibrary(pathlibrary)
        prompt = input("Would you like to store the path library as JSON file: Y/n ")
        if checkoption(prompt):
            createJSON(pathlibrary)
        else:
            prompt = input("Your current path library will NOT be saved, is that okay: Y/n ")
            if checkoption(prompt):
                openallpaths(pathlibrary)
            else:
                createJSON(pathlibrary)
    else:
        print("Current path library: empty!")

    print("Goodbye...")
    quit()


# creates JSON file from path library data
def createJSON(lib_data):
    if lib_data:
        title = input("Enter title for the new JSON file: ")
        with open(title+'.json', 'w') as fp:
            json.dump(lib_data, fp)
    else:
        print("The path library is currently empty!")
        print("Please add paths to the library")
        start()


# using JSON file as path library
def usepathlibrary():
    jsonfile = Path(dictpath())
    if jsonfile.is_file():
        location = str(jsonfile.resolve())
        try:
            mypathlib = json.load(open(location))
            print("Success! Using: " + str(jsonfile))
            return mypathlib
        except ValueError:
            print("This is not a JSON file, please try again")
            usepathlibrary()
    else:
        print("Cannot not locate JSON file, please try again")
        usepathlibrary()


# allows user to load by JSON or SQLite
def selectpathlibrary():
    prompt = input("Do you already have a path library: Y/n ")
    if checkoption(prompt):
        prompt = input("Are you using a SQLite Database: Y/n ")
        if checkoption(prompt):
            print("make connection...") # Coming soon SQLite connection ...
        else:
            print("Looking for JSON file...")
            json_dict = usepathlibrary()
            pathlibrary.update(json_dict)
    else:
        prompt = input("Would you like to create a new path library: Y/n ")
        if checkoption(prompt):
            start()
        else:
            print("Goodbye...")
            quit()


# loads all dictionaries, adds contents to a list, and then adds that list to the main list
def openallpaths(pathlib):
    mainlist = []
    for key, path, in pathlib.items():
        thislist = []
        print("Opening: " + key)
        dict_contents = open(path, 'r')
        for word in dict_contents:
            thislist.append(word.rstrip())
        mainlist.append(thislist)
        dict_contents.close()

# start of application
def start():
    single()
    multiple()


selectpathlibrary()
start()
