if __name__ == "__main__":
    import create
    import exists
    import option

    path_lib = dict()

    finished_loading = False
    while finished_loading is False:

        if option.existing_path_lib() is True:
            existing = exists.load_json()
            path_lib = existing.get_path_lib()
            if option.display_path_lib_prompt() is True:
                existing.display_path_lib()

        elif option.create_path_lib_prompt() is True:
            created = create.new_path_lib()
            done = False
            while not done:
                created.prompt()
                if create.add_another_path() is False:
                    done = True
            path_lib = created.get_path_lib()
            if option.display_path_lib_prompt() is True:
                created.display_path_lib()
            if create.save_as_json_prompt() is True:
                created.create_json()
            else:
                if create.not_saved_json_prompt() is False:
                    created.create_json()

        elif option.use_default_prompt() is True:
            path_lib = exists.use_default()
            finished_loading = True

        else:
            if option.quit_game_prompt() is True:
                print("Goodbye...")
                quit()