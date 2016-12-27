# File: library.py
import glob
import json
import random
from pathlib import Path

path_library = dict()  # our path library
word_bank = []  # list of words
key_chain = []  # list of keys
possible_words = []  # list of possible words
initial_word = []  # word that we are using


# returns boolean from user input
def to_boolean(option):
    if option.startswith("Y") or option.startswith("y"):
        return True
    else:
        return False
    

# locates file(s) and returns a list
def locate_files(path):
    found = glob.glob(path)
    return found


# calls create() after successfully adding a path to path library
def add_more_dictionaries():
    prompt = input("Would you like to add more paths to library: Y/n ")
    if to_boolean(prompt) is True:
        create()
    else:
        print("phase 2, line 30")


# prompts user to enter path
def enter_path():
    path = input("Enter path: ")
    return path


# displays the contents of the path library
def show_path_lib(lib):
    for k, v in lib.items():
        print("Key: [" + k + "] " + "Path: [" + v + "]")


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
def add_path(dictionary):
    for val in dictionary:
        check = False
        while not check:
            print("For this path: " + val)
            key = input("Please enter a unique key to identify it: ")
            print("Key:", key, ", Path:", val)
            prompt = input("Is this information correct: Y/n ")
            if to_boolean(prompt) is True:
                path_library.update({key: val})
                check = True
            else:
                check = False
    print("Added!")
    add_more_dictionaries()


# adds path to a single dictionary to path library
def single_path():
    value = authenticate("file", single_path)
    found = locate_files(value)
    add_path(found)


# adds path to an entire directory of dictionaries to path library
def directory_path():
    value = authenticate("directory", directory_path)
    if value.endswith("/"):
        new_path = value + "*"
        found = locate_files(new_path)
        add_path(found)
    else:
        new_path = value + "/*"
        found = locate_files(new_path)
        add_path(found)


# adds paths of dictionaries by extension to path library
def extension_path():
    value = authenticate("extension", extension_path)
    extension = input("Enter file extension to use: ")
    new_path = value + "/*" + extension
    found = locate_files(new_path)
    add_path(found)


# creates JSON file from path library data
def create_json(lib_data):
    title = input("Enter title for the new JSON file: ")
    with open(title + '.json', 'w') as fp:
        json.dump(lib_data, fp)


# prompts to display "path_library" variable
def display_current_library():
    print("Current path library size: " + str(len(path_library)))  # shows how many dictionaries are in the path library
    show_path_lib(path_library)  # displays keys and paths


# finds JSON dictionary contents and converts it for python use
def json_dict_to_python():
    json_file = Path(enter_path())  # prompts user to enter path
    if json_file.is_file():
        file_location = str(json_file.resolve())
        try:
            json_dictionary = open(file_location)
            python_dictionary = json.load(json_dictionary)
            print("Success! Using: " + str(json_file))
            json_dictionary.close()
            return python_dictionary
        except ValueError:
            print("This is not a JSON file, please try again")
            json_dict_to_python()
    else:
        print("Cannot not locate JSON file, please try again")
        json_dict_to_python()


# allows user to use a SQLite Database
def load_database():
    print("make connection...")  # Coming soon SQLite connection ...


# allows user to use a JSON file
def load_json_file():
    python_dict = json_dict_to_python()
    path_library.update(python_dict)  # adds contents to global dictionary


# questions if the user wants to use an existing path library
def load():
    prompt = input("Are you using a SQLite Database: Y/n ")
    if to_boolean(prompt) is True:
        load_database()  # access database
    else:
        print("Looking for JSON file...")
        load_json_file()  # access json file


# creates a new JSON file based on user input
def create():
    option = input("Add a single dictionary to new path library: Y/n ")  # using a single dictionary
    if to_boolean(option) is True:
        single_path()

    option = input("Add entire directory of dictionaries to new path library: Y/n ")  # using entire directory
    if to_boolean(option) is True:
        directory_path()

    option = input("Add dictionaries by extension to new path library: Y/n ")  # using dictionaries by extension
    if to_boolean(option) is True:
        extension_path()


# beginning of the application
def start():
    prompt = input("Do you already have a path library: Y/n ")  # prompts to load existing path library
    if to_boolean(prompt) is True:
        load()

    prompt = input("Would you like to create a new path library: Y/n ")  # prompts to create a new JSON file
    if to_boolean(prompt) is True:
        create()

    if path_library:
        prompt = input("Would you like to see the value(s) in the path library? Y/n ")  # prompts to show value and size
        if to_boolean(prompt) is True:
            display_current_library()

        prompt = input("Would you like to store this path library as new JSON file: Y/n ")  # store new JSON file
        if to_boolean(prompt) is True:
                create_json(path_library)  # creates new JSON file
        else:  # no save
            prompt = input("Your current path library will NOT be saved, is that okay: Y/n ")
            if to_boolean(prompt) is True:
                use_all_dictionaries(path_library, word_bank)
            else:
                create_json(path_library)
    else:  # empty
        print("The current library is empty!")
        print("Please add/load dictionaries!")

    prompt = input("Would you like to quit: Y/n ")
    if to_boolean(prompt) is True:
        print("Goodbye...")
        quit()
    else:
        start()

start()


# takes words from dictionary and adds them to the list
def populate_list(dictionary):
    store = []
    for word in dictionary:
        store.append(word.rstrip())
    return store


# loads all words from all dictionaries and add them to the list "word_bank"
def use_all_dictionaries(library, word_list):
    for key, path, in library.items():
        print("Opening: " + key)
        dict_contents = open(path, 'r')
        store = populate_list(dict_contents)
        dict_contents.close()
        word_list.append(store)
        key_chain.append(key)


# loads specific dictionaries by a key
def use_dictionary_by_key(library, word_list, key_list):
    chosen = input("Please enter a key: ")
    if chosen not in key_list:
        if chosen in library:
            key_list.append(chosen)
            for key, path in library.items():
                if chosen == key:
                    dict_contents = open(path, 'r')
                    store = populate_list(dict_contents)
                    dict_contents.close()
                    word_list.append(store)
        else:
            print("Could not find key, please try again")
            use_dictionary_by_key(library, word_list, key_list)
    else:
        print("You have already used this key!")


# displays all of the available keys in the library
def display_keys(library, key_list):
    for key in library.items():
        print("Library Key: " + key)
    if key_list:
        for key in key_list:
            print("Used Key: " + key)
    else:
        print("Used Keys: none")


# randomly selects a word and scrambles selected word
def scramble(word_list):
    selected = random.choice(word_list)
    charlist = list(selected)
    random.shuffle(charlist)
    scrambled = ''.join(charlist)
    retval = list(scrambled)
    return retval


# checks if word length is valid
def valid_length(word_list):
    smallest = min(len(word) for word in word_list)
    longest = max(len(word) for word in word_list)
    print("Smallest: " + smallest + ", Longest: " + longest)
    try:
        num = int(input("Please enter a number: "))
        if smallest <= num <= longest:
            return num
        else:
            valid_length(word_list)
    except ValueError:
        print("Not a valid number")
        valid_length(word_list)


# returns a list of possible words based on length
def word_by_length(length, word_list):
    possible = []
    for word in word_list:
        if len(word) == length:
            possible.append(word)
    return possible


# finds all possible words
def find_possible_words(character_list, word_list, possible):
    for letter in character_list:
        for word in word_list:
            if word.startswith(letter):
                possible.append(word)
    for possible_word in possible:
        p_char_list = list(possible_word)
        for p_letter in p_char_list:
            if p_letter not in character_list:
                possible.remove(possible_word)


# hides word by putting an underscore for each letter
def hide_words(approved_list):
    sorted(approved_list)
    dashes = []
    for word in approved_list:
        temp = ""
        for letter in word:
            temp.join("_")
        dashes.append(temp)
    print(dashes)


# uses the word bank
def use_word_bank():
    chosen_length = valid_length(word_bank)
    starting_words = word_by_length(chosen_length, word_bank)
    chosen_word = scramble(starting_words)
    initial_word.append(chosen_word)
    print(initial_word)
    find_possible_words(chosen_word, word_bank, possible_words)
    hide_words(possible_words)


def implementation():
    prompt = input("Would you like to use all the dictionaries in the library: Y/n ")
    if to_boolean(prompt) is True:
        use_all_dictionaries(path_library, word_bank)  # adds words to "word_bank" list

    prompt = input("Would you like to select dictionaries to use by key: Y/n ")
    if to_boolean(prompt) is True:
        another_one = True
        while another_one is True:
            display_keys(path_library, key_chain)
            use_dictionary_by_key(path_library, word_bank, key_chain)  # adds words to "word_bank" list
            prompt = input("Would you like to use another key: Y/n ")
            if to_boolean(prompt) is False:
                another_one = False

    prompt = input("Would you like to start: Y/n ")
    if to_boolean(prompt) is True:
        use_word_bank()


