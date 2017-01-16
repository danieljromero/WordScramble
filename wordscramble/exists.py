# File: exists.py
import json
import option
from pathlib import Path


def sqlite_prompt():  # future implementation
    answer = input("Do you have a SQLite Database full of words: " + option.yes_or_no())
    return option.interpret(answer)


def load_json_prompt():  # future implementation
    answer = input("Do you have already have a path library JSON file: " + option.yes_or_no())
    return option.interpret(answer)


def json_dict_to_python():
    """
    Transforms json to a dictionary in python
    :return: json to a dictionary in python
    """
    json_found = False
    while json_found is False:
        json_file = Path(option.enter_path())
        if json_file.is_file():
            file_location = str(json_file.resolve())
            try:
                json_dictionary = open(file_location)
                python_dictionary = json.load(json_dictionary)
                print("Success! Using: \"" + file_location.rsplit("/", 1)[-1] + "\"")
                json_dictionary.close()
                return python_dictionary
            except ValueError:
                print("This is not a JSON file, please try again")
        else:
            print("Cannot not locate JSON file, please try again")


def use_default():
    """
    Allows user to use the default path library if the user would like to do so
    :return: default path library to python dictionary
    """
    default_file = Path("../json/default/default.json")
    default_path = str(default_file.resolve())
    json_dict = open(default_path)
    python_dict = json.load(json_dict)
    json_dict.close()
    return python_dict


class load_json:

    def __init__(self):
        self.path_lib = json_dict_to_python()

    def get_path_lib(self):
        return self.path_lib

    def display_path_lib(self):
        print("Path Library: " + str(self.path_lib))
