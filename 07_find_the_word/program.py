import os


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Please provide a valid location.")
        return

    word = get_search_word_from_user()
    if not word:
        print("Please provide a word to search for.")
        return

    matches = search_folders(folder, word)

    for match in matches:
        print(match)


def print_header():
    print('FIND THE WORD')


def get_folder_from_user():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_word_from_user():
    word = input('What word would you like to find? ')
    return word.lower()


def search_folders(folder, word):

    all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            continue

        matches = search_file(full_item, word)
        all_matches.extend(matches)

    return all_matches


def search_file(filename, word):
    matches = []

    with open(filename, 'r', encoding='utf-8') as fin:

        for line in fin:
            if line.lower().find(word) >= 0:
                matches.append(line)

        return matches


if __name__ == '__main__':
    main()
