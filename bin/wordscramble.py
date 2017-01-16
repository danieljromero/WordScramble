# File: wordscramble.py
import sys

sys.path.append("../wordscramble/")


def goodbye():
    print("Goodbye...")
    quit()

if __name__ == "__main__":

    import create
    import exists
    import option
    import game

    path_lib = dict()

    finished_loading = False
    while finished_loading is False:
        if option.existing_path_lib() is True:
            existing = exists.load_json()
            path_lib = existing.get_path_lib()
            if option.display_path_lib_prompt() is True:
                existing.display_path_lib()
            finished_loading = True
        elif option.create_path_lib_prompt() is True:
            created = create.new_path_lib()
            done = False
            while not done:
                created.prompt()
                if create.add_another_path() is False:
                    done = True
            path_lib = created.get_path_lib()  # path library
            if option.display_path_lib_prompt() is True:
                created.display_path_lib()
            if create.save_as_json_prompt() is True:
                created.create_json()
            else:
                if create.not_saved_json_prompt() is False:
                    created.create_json()
            finished_loading = True
        elif option.use_default_prompt() is True:
            path_lib = exists.use_default()
            finished_loading = True
        else:
            if option.quit_game_prompt() is True:
                goodbye()

    play_again = True
    while play_again is True:
        if game.start_prompt() is True:
            new_game = game.word_scramble(path_lib)
            new_game.use_all()
            new_game.start()
            if game.play_again_prompt() is False:
                goodbye()
        else:
            if option.quit_game_prompt() is True:
                goodbye()
