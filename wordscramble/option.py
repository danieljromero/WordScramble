def interpret(user_input):
    """
    Takes user input and returns a boolean, defaults to false
    :param user_input
    :return: true if user entered "Y" or "y", false if otherwise or empty
    """
    if user_input.startswith("Y") or user_input.startswith("y"):
        return True
    else:
        return False


def yes_or_no():
    """
    Generates y/n option, defaults to "No"
    :return: y/n option, defaults to "No"
    """
    return "[y/N] "


def yes_or_no2():
    """
    Generates y/n option, defaults to "Yes"
    :return: y/n option, defaults to "Yes"
    """
    return "[Y/n] "


def enter_path():
    """
    User provides path
    :return: path
    """
    path = input("Enter path: ")
    return path


def create_path_lib_prompt():
    """
    Asks user if they would like to create a new path lib
    :return: True or False based on users input
    """
    answer = input("Would you like to create a new path library: " + yes_or_no())
    return interpret(answer)


def existing_path_lib():
    """
    Asks user if path library already exists
    :return: True or False based on users input
    """
    answer = input("Do you already have a path library: " + yes_or_no())
    return interpret(answer)


def use_default_prompt():
    """
    Asks users if they would like to use the default path library
    :return: True or False based on users input
    """
    answer = input("Would you like to use the default path library: " + yes_or_no())
    return interpret(answer)


def display_path_lib_prompt():
    """
    Asks user if they want to see the contents of the current Path Library
    :return: True or False based on users input
    """
    answer = input("Would you like to see the contents of the current path library: " + yes_or_no())
    return interpret(answer)


def quit_game_prompt():
    """
    Asks user if they want to quit
    :return: True or False based on users input
    """
    answer = input("Would you like to quit:" + yes_or_no())
    return interpret(answer)