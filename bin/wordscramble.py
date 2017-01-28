# File: wordscramble.py
import click
import random
import re
from collections import OrderedDict


def extract(text_file):
    """Creates a set of words from a text file

    Opens and reads a text file, extracts the data and turns it into a stripped set of words to avoid any duplicates.
    Program will yell at you if the text file has one or no words in it.

    Args:
        :param text_file: Instance of a file with (hopefully) extension .txt

    Returns:
        :return: A set of extracted words from text file

    Raises:
        :raise: ValueError: An error occurred accessing file contents
        :raise: ValueError: Error occurred because file contents are minimal or non-existent
    """
    try:
        file = open(text_file, 'r')  # open and read text file
    except ValueError:
        print("Cannot open text file, please try again")
    else:
        word_set = set([word.lower().rstrip() for word in file])  # avoid duplicates
        file.close()  # close text file
        if len(word_set) <= 1:
            raise ValueError("\"{}\" does not contain enough words".format(text_file))
        else:
            return word_set


def select_word(length, word_set):
    """Randomly selects a word from a WordSet.

    Creates a list of all the words from a WordSet that match the length desired, then randomly selects one as the
    original word for the game.

    Args:
        :param length: An integer representing the length of the word to find
        :param word_set: A set of words instance

    Returns:
        :return: A randomly selected word from a list of words of a certain length
    """
    possible_words = [word for word in word_set if len(word) == length]  # list of words of a certain length
    return random.choice(possible_words)  # returns random word from list


def scramble(word):
    """Randomly orders a word.

    Transforms word into a list of characters then shuffle's them and then reassembles the list back into a string.

    Args:
        :param word: The string to scramble

    Returns:
        :return: Randomly ordered string
    """
    char_list = list(word)  # list of characters in a word
    random.shuffle(char_list)  # shuffles word
    scrambled = ''.join(char_list)  # reassembles string
    return scrambled


def analyze(word):
    """Calculates the amount of occurances for each letter in a word.

    Creates a dictionary for each letter in the word along with its amount of repetitions.

    Args:
        :param word: string to analyze

    Return:
        :return: a dictionary, dict() object, with each letter in a word as keys and the amount of repetitions as values
    """
    word_list = list(enumerate(word))  # creates a list of occurrences
    results = dict()  # dictionary to store keys, and values
    for index, letter in word_list:
        count = 1  # every letter in word occurs at least once
        for i, character in word_list:
            if i != index and letter == character:
                count += 1
        if letter not in results:
            results.update({letter: count})
    return results


def valid_occurrences(word_stats, main_stats):
    """Checks if each the word contains the correct number of letter repetitions.

    Returns true if word contains correct number of characters based on word stats, false if otherwise.

    Args:
        :param word_stats: dict() of letters and their repetitions
        :param main_stats: dict() of stats from the chosen word we are comparing

    Return:
        :return: True if word falls within the correct parameters, False if otherwise
    """
    for key in word_stats:
        main_value = main_stats.get(key)
        new_value = word_stats.get(key)
        if new_value > main_value:
            return False
    return True


def find_possible_words(selected_word, word_list, max_length):
    """Uses the selected word and finds the words that can be used.

    Uses the word to compare other words too with the correct lengths.

    Args:
        :param selected_word: word we are comparing
        :param word_list: list of words
        :param max_length: difficulty

    Return:
        :return: Set of possible words
    """
    main_stats = analyze(selected_word)  # gets the dictionary representation of letters and number of repetition
    pw = [word for word in word_list if len(word) <= max_length and not set(word) - set(selected_word)]
    possible_words = set([word for word in pw if valid_occurrences(analyze(word), main_stats) is True])
    return possible_words


def hide_word(word):
    """Creates a word by creating an underscore representation.

    Uses the length of the string and then creates a string of underscores for the word.

    Args:
        :param word: string we are planning to hide

    Return:
        :return: sequence of underscores based on string length
    """
    underscore = "_" * len(word)
    return underscore


def dictionary_of_answers(word_set):
    """Uses a set of words and associates it with a dictionary.

    Creates a dictionary with the key representing the correct words and the value as the underscore representation.

    Args:
        :param word_set: set of possible words

    Return:
        :return: Ordered dictionary of keys: answers, value: underscore representation
    """
    sort_alphabetically = sorted(word_set)  # sorts alphabetically
    sort_by_length = sorted(sort_alphabetically, key=len)  # sorts by length
    dashes = [hide_word(word) for word in sort_by_length]  # generates list of underscore's
    answers = OrderedDict(zip(sort_by_length, dashes))  # preserves ordering for display
    return answers


def string_decorator(string):
    """A decorator for reuse.

    Decorates a print() function.

    Args:
        :param string: string to decorate
    """
    print("=" * len(string))
    print(string)
    print("=" * len(string))


def game(answers, word):
    """Actual game

    Checks if the game is over, checks guesses, keep tracks of incorrect guesses and other functions.

    Args:
        :param answers: dictionary of correct words
        :param word: word we are unscrambling
    """
    game_over = len(answers)  # number of answers to get correct
    correct = set()  # holds correct guesses
    incorrect = set()  # holds incorrect guesses

    print("Press \"q\" to quit, \"v\" to view incorrect guesses")  # prompt option to quit

    while len(correct) < game_over:  # if the number of correct guesses do not match the number of correct answers
        for value in answers:
            print(answers.get(value))
        string_decorator("Unscramble: \""+word+"\"")  # word to unscramble

        guess_prompt = "-> Guess Word: "
        guess = input(guess_prompt)

        while not guess:  # null check
            guess = input(guess_prompt)

        if guess in answers and guess not in correct:
            correct.add(guess)  # adds correct guess to correct set()
            answers[guess] = guess  # shows the correct guess
        elif guess == "v":  # prompts for view
            if incorrect:
                string_decorator("Previous Guesses: " + str(incorrect))
            else:
                string_decorator("Previous Guesses: None")
        elif guess == "q":  # prompts to quit and game over
            for key in answers:
                print(key)
            string_decorator("Game Over")
            break
        else:  # adds guess to incorrect
            incorrect.add(guess)

    print("Correct Guesses: " + str(len(correct)) + "/" + str(game_over))  # shows result from game
    if len(correct) == game_over:  # winner prompt
        print("Congratulations! You win!")


@click.command()
@click.argument('dictionary', type=click.Path(exists=True))
@click.argument('max_length', type=int)
def main(dictionary, max_length):
    """Command Line Word Game using Python3 and dictionaries"""
    initial_set = extract(dictionary)  # set of words, no duplicates
    actual_length = max(len(word) for word in initial_set)  # finds longest word length, int
    if max_length <= actual_length:  # checks if user input: "max_length" is within range
        original_word = select_word(max_length, initial_set)  # uses max_length to find word
    else:
        original_word = select_word(actual_length, initial_set)  # calculates and uses the actual largest length
    pattern = "^["+original_word+"]{1,"+str(len(original_word))+"}$"  # "^[xyz]{1,n}" checks first character and length
    regex = re.compile(pattern, re.IGNORECASE)
    results = [match.group(0) for word in initial_set for match in [regex.match(word)] if match]
    scrambled = scramble(original_word)
    if scrambled == original_word:  # makes sure words aren't similar
        while scrambled == original_word:
            scrambled = scramble(original_word)
    possible_word_set = find_possible_words(scrambled, results, max_length)
    #print("Answers: " + str(possible_word_set))  # to see answers
    answers = dictionary_of_answers(possible_word_set)
    game(answers, scrambled)  # starts game