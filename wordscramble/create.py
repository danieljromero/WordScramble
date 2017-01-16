# File: create.py
import shutil
import json
import option
import glob
from pathlib import Path


def single_path_prompt():
    answer = input("Add a single dictionary to new path library: " + option.yes_or_no())
    return option.interpret(answer)


def directory_path_prompt():
    answer = input("Add entire directory of dictionaries to new path library: " + option.yes_or_no())
    return option.interpret(answer)


def extension_path_prompt():
    answer = input("Add dictionaries by extension to new path library: " + option.yes_or_no())
    return option.interpret(answer)


def add_another_path():
    answer = input("Would you like to add another dictionary to the path library: " + option.yes_or_no())
    return option.interpret(answer)


def save_as_json_prompt():
    answer = input("Would you like to store this path library as a new JSON file: " + option.yes_or_no())
    return option.interpret(answer)


def not_saved_json_prompt():
    answer = input("Your current path library will NOT be saved, is that okay: " + option.yes_or_no())
    return option.interpret(answer)


def enter_dictionary_location():
    """
    Prompts user to enter a dictionary location
    :return: string representation of dictionary location
    """
    dictionary_found = False
    while dictionary_found is False:
        answer = option.enter_path()  # prompt
        full_path = Path(answer)
        if full_path.is_file():
            print("This is a file!")
            paths = str(full_path.resolve())
            return paths
        elif full_path.is_dir():
            print("This is a directory!")
            paths = str(full_path.resolve())
            return paths
        else:
            print("Could not locate dictionary, please try again")


def locate_files(paths):
    """
    Uses paths to return dictionaries as a list
    :param paths:
    :return: list of paths
    """
    path_list = glob.glob(paths)
    return path_list


def add_path(path_list, path_library):
    """
    Assigns keys to paths in "path_list" and appends them to path_library
    :param path_list:
    :param path_library:
    """
    for path in path_list:
        check = False
        while not check:
            print("For this path: " + path)
            key = input("Please enter a unique key to identify it: ")
            if key not in path_library and len(key) > 0:
                print("Key:", key, ", Path:", path)
                answer = input("Is this information correct: " + option.yes_or_no())
                if option.interpret(answer) is True:
                    path_library.update({key: path})
                    print("Added!")
                    check = True
                else:
                    check = False
            else:
                print("Not a unique key, please try another identifier")
                check = False


class new_path_lib:

    def __init__(self):
        self.path_lib = dict()

    def get_path_lib(self):
        """
        Gets path_lib
        :return: path_lib
        """
        return self.path_lib

    def display_path_lib(self):
        print("Path Library: " + str(self.path_lib))

    def prompt(self):
        if single_path_prompt() is True:
            single_dictionary_path = enter_dictionary_location()
            single_path_list = locate_files(single_dictionary_path)
            add_path(single_path_list, self.path_lib)

        elif directory_path_prompt() is True:
            directory_path = enter_dictionary_location()
            if directory_path.endswith("/"):
                new_path = directory_path + "*"
                directory_path_list = locate_files(new_path)
                add_path(directory_path_list, self.path_lib)
            else:
                new_path = directory_path + "/*"
                directory_path_list = locate_files(new_path)
                add_path(directory_path_list, self.path_lib)

        elif extension_path_prompt() is True:
            print("Please provide path to the directory first!")
            extension_path = enter_dictionary_location()
            extension = input("Enter file extension to use: ")
            new_path = extension_path + "/*" + extension
            extension_path_list = locate_files(new_path)
            add_path(extension_path_list, self.path_lib)

    def create_json(self):
        title = input("Enter title for the new JSON file: ")
        json_file_name = title + '.json'
        with open(json_file_name, 'w') as output:
            json.dump(self.path_lib, output)
        output.close()
        destination = Path("../json/")
        json_folder = str(destination.resolve())
        shutil.move(json_file_name, json_folder)
        print("Saved to directory: \"" + json_folder + "/\"")

