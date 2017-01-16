# File: game.py
import random
import option
from collections import OrderedDict


def start_prompt():
    answer = input("Ready to start: " + option.yes_or_no())
    return option.interpret(answer)


def play_again_prompt():
    answer = input("Play again: " + option.yes_or_no())
    return option.interpret(answer)


def select_difficulty_prompt(word_list):
    """
    Allows user to set the difficulty depending on the length of characters provided
    :param word_list: scans through list to retrieve data
    :return: difficulty
    """
    shortest = min(len(word) for word in word_list)
    longest = max(len(word) for word in word_list)
    again = True
    while again is True:
        if shortest == longest:
            print("All words are the same length!")
            return shortest
        else:
            print("Shortest word: " + str(shortest) + ", Longest word: " + str(longest))
            print("\"The smaller the number the easier the game will be!\"")
            try:
                difficulty = int(input("Please enter a number: "))
                if shortest <= difficulty <= longest:
                    return difficulty
                else:
                    print("Please select a number in between {} and {}!".format(shortest, longest))
            except ValueError:
                print("Not a valid number!")


def starting_words_list(difficulty, word_set):
    """
    Returns all of the words that match the selected difficulty
    :param difficulty: integer
    :param word_set: set containing all words to choose from
    :return: list of strings that will randomly be selected
    """
    possible_words = []
    for word in word_set:
        if len(word) == difficulty:
            possible_words.append(word)
    return possible_words


def random_select(word_list):
    """
    Randomly selects word from word list
    :param word_list: list of words we are choosing from
    :return: selected word
    """
    selected = random.choice(word_list)
    return selected


def scramble(word):
    """
    Randomly orders the word
    :param word: string
    :return: Randomly ordered string
    """
    char_list = list(word)
    random.shuffle(char_list)
    scrambled = ''.join(char_list)
    return scrambled


def analyze(word):
    """
    Analyzes word for how many character representation it may have
    :param word: string to analyze
    :return: dict() of results from word
    """
    word_list = list(enumerate(word))
    results = dict()
    for index, letter in word_list:
        count = 1
        for i, character in word_list:
            if i != index and letter == character:
                count += 1
        if letter not in results:
            results.update({letter: count})
    return results


def valid_occurrences(word_stats, main_stats):
    """
    Returns true if word contains correct number of characters based on word stats
    :param word_stats: dict() of stats from a word
    :param main_stats: dict() of stats from the chosen word we are comparing
    :return: True if word falls within the correct parameters, False if otherwise
    """
    for key in word_stats:
        main_value = main_stats.get(key)
        new_value = word_stats.get(key)
        if new_value > main_value:
            return False
    return True


def find_possible_words(selected_word, word_list, max_length):
    """
    Uses the selected word and selects words that can be used
    :param selected_word: word we are comparing
    :param word_list: list of words
    :param max_length: difficulty
    :return: Set of possible words
    """
    main_stats = analyze(selected_word)
    pw = [word for word in word_list if len(word) <= max_length and not set(word) - set(selected_word)]
    possible_words = set([word for word in pw if valid_occurrences(analyze(word), main_stats) is True])
    print(possible_words)
    return possible_words


def underscore_representation(word):
    """
    Creates a word that is hidden by underscores
    :param word: string we are hiding
    :return: sequence of underscores based on string length
    """
    underscore = "_" * len(word)
    return underscore


def hide_words(word_set):
    """
    Creates a dictionary with the key representing the correct word and the value as the underscore representation
    :param word_set: set of possible words
    :return: Ordered dictionary of keys: answers, value: underscore representation
    """
    sort_alphabetically = sorted(word_set)
    sort_by_length = sorted(sort_alphabetically, key=len)
    dashes = [underscore_representation(word) for word in sort_by_length]  # generates list of underscore's
    answers = OrderedDict(zip(sort_by_length, dashes))  # preserves ordering for display
    return answers


def string_decorator(string):
    """
    decorates string
    :param string: string to decorate
    """
    print("=" * len(string))
    print(string)
    print("=" * len(string))


def game(answers, word):
    """
    Actual game that checks if the game is over, checks guesses, keep tracks of incorrect guesses abd other functions
    :param answers: dictionary of correct words
    :param word: word we are unscrambling
    """
    game_over = len(answers)
    correct = set()
    incorrect = set()
    print("Press \"q\" to quit, \"v\" to view incorrect guesses")
    while len(correct) < game_over:
        for value in answers:
            print(answers.get(value))
        string_decorator("Unscramble: \""+word+"\"")
        guess_prompt = "-> Guess Word: "
        guess = input(guess_prompt)
        while not guess:
            guess = input(guess_prompt)
        if guess in answers and guess not in correct:
            correct.add(guess)
            answers[guess] = guess
        elif guess == "v":
            if incorrect:
                string_decorator("Previous Guesses: " + str(incorrect))
            else:
                string_decorator("Previous Guesses: None")
        elif guess == "q":
            for key in answers:
                print(key)
            string_decorator("Game Over")
            break
        else:
            incorrect.add(guess)
    print("Correct Guesses: " + str(len(correct)) + "/" + str(game_over))
    if len(correct) == game_over:
        print("Congratulations! You win!")


class word_scramble:

    def __init__(self, library):
        self.library = library
        self.word_set = set()

    def use_all(self):
        """
        Method that loads all of the words from all of the dictionaries in the library
        """
        for key, path in self.library.items():
            print("Using: \"" + key + "\"")
            dict_contents = open(path, 'r')
            for word in dict_contents:
                self.word_set.add(word.rstrip())
            dict_contents.close()

    def start(self):
        difficulty = select_difficulty_prompt(self.word_set)
        starting_words = starting_words_list(difficulty, self.word_set)
        chosen_word = random_select(starting_words)
        scrambled = scramble(chosen_word)
        possible_word_set = find_possible_words(scrambled, self.word_set, difficulty)
        answers = hide_words(possible_word_set)
        game(answers, scrambled)
