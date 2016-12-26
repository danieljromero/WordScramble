# File: library.py
import glob
import json
import random
from pathlib import Path

path_library = dict()  # our path library


# returns boolean from user input
def check_option(option):
    if option.startswith("Y") or option.startswith("y"):
        return True
    else:
        return False
    

# locates file(s) and returns a list
def locate_files(path):
    found = glob.glob(path)
    return found


# calls start() after successfully adding a path to path library
def start_over(method):
    prompt = input("Would you like to add more paths to library: Y/n ")
    if check_option(prompt):
        method()
    else:
        print("continuing...")
        scanned = load_all_paths(path_library)


# prompt
def enter_path():
    path = input("Enter path: ")
    return path


# displays the contents of the path library
def show_path_lib(lib):
    for k, v in lib.items():
        print("Key: ["+ k +"] " + "Path: [" + v + "]")


# gets user input and returns the correct path value
def authenticate(message, method):
    value = Path(enter_path())
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


# adds dictionary path to the path library
def add_path(list):
    for val in list:
        check = False
        while not check:
            print("For this path: " + val)
            key = input("Please enter a unique key to identify it: ")
            print("Key:", key, ", Path:", val)
            prompt = input("Is this information correct: Y/n ")
            if check_option(prompt):
                path_library.update({key: val})
                check = True
            else:
                check = False
    print("Added!")
    start_over()


# adds path to a single dictionary to path library
def single_path():
    value = authenticate("file", single_path)
    found = locate_files(value)
    add_path(found)


# adds path to an entire directory of dictionaries to path library
def directory_path():
    value = authenticate("directory", directory_path)
    if value.endswith("/"):
        newpath = value + "*"
        found = locate_files(newpath)
        add_path(found)
    else:
        newpath = value + "/*"
        found = locate_files(newpath)
        add_path(found)


# adds paths of dictionaries by extension to path library
def extension_path():
    value = authenticate("extension", extension_path)
    extension = input("Enter file extension to use: ")
    newpath = value + "/*" + extension
    found = locate_files(newpath)
    add_path(found)


# single dictionary option
def single():
    option = input("Add a single dictionary to new path library: Y/n ")
    if check_option(option):
        single_path()


# multiple dictionaries option
def multiple():
    option = input("Add entire directory of dictionaries to new path library: Y/n ")
    if check_option(option):
        directory_path()

    option = input("Add dictionaries by extension to new path library: Y/n ")
    if check_option(option):
        extension_path()

    if path_library:
        print("Current path library size: " + str(len(path_library)))
        prompt = input("Would you like to see the value(s) in the path library? Y/n ")
        if check_option(prompt):
            show_path_lib(path_library)
        prompt = input("Would you like to store the path library as JSON file: Y/n ")
        if check_option(prompt):
            create_json(path_library)
        else:
            prompt = input("Your current path library will NOT be saved, is that okay: Y/n ")
            if check_option(prompt):
                load_all_paths(path_library)
            else:
                create_json(path_library)
    else:
        print("Current path library: empty!")

    print("Goodbye...")
    quit()


# creates JSON file from path library data
def create_json(lib_data):
    if lib_data:
        title = input("Enter title for the new JSON file: ")
        with open(title+'.json', 'w') as fp:
            json.dump(lib_data, fp)
    else:
        print("The path library is currently empty!")
        print("Please add paths to the library")
        start()


# using JSON file as path library
def json_path():
    jsonfile = Path(enter_path())
    if jsonfile.is_file():
        location = str(jsonfile.resolve())
        try:
            mypathlib = json.load(open(location))
            print("Success! Using: " + str(jsonfile))
            return mypathlib
        except ValueError:
            print("This is not a JSON file, please try again")
            json_path()
    else:
        print("Cannot not locate JSON file, please try again")
        json_path()


# allows user to load by JSON or SQLite
def load_json_file():
    prompt = input("Do you already have a path library: Y/n ")
    if check_option(prompt):
        prompt = input("Are you using a SQLite Database: Y/n ")
        if check_option(prompt):
            print("make connection...")  # Coming soon SQLite connection ...
        else:
            print("Looking for JSON file...")
            json_dict = json_path()
            path_library.update(json_dict)
    else:
        prompt = input("Would you like to create a new path library: Y/n ")
        if check_option(prompt):
            start()
        else:
            print("Goodbye...")
            quit()


# takes words from dictionary and adds them to the list
def populate_list(dictionary):
    list = []
    for word in dictionary:
        list.append(word.rstrip())
    return list


# loads all dictionaries, adds contents to a list, and then adds that list to the main list
def load_all_paths(pathlib):
    mainlist = []
    for key, path, in pathlib.items():
        thislist = []
        print("Opening: " + key)
        dict_contents = open(path, 'r')
        for word in dict_contents:
            thislist.append(word.rstrip())
        mainlist.append(thislist)
        dict_contents.close()
    return mainlist


# loads specific dictionaries by a key
def load_path_by_key(chosen, pathlib):
    mainlist = []
    for key, path in pathlib.items():
        if chosen == key:
            dict_contents = open(path, 'r')
            store = populate_list(dict_contents)
            dict_contents.close()
        mainlist.append(store)
    return mainlist


# randomly selects and scrambles word
def scramble(list):
    selected = random.choice(list)
    charlist = list(selected)
    random.shuffle(charlist)
    scrambled = ''.join(charlist)
    retVal = list(scrambled)
    return retVal


# start of application
def start():
    single()
    multiple()


load_json_file()
start()
