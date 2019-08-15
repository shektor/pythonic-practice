import os


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Please provide a valid location.")
        return

    text = get_search_text_from_user()
    if not text:
        print("Please provide a word to search for.")
        return

    search_file(folder, text)


def print_header():
    print('FIND THE WORD')


def get_folder_from_user():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What word would you like to find? ')
    return text


def search_file(folder, text):
    print("Would search '{}' for the word '{}'".format(folder, text))


if __name__ == '__main__':
    main()
