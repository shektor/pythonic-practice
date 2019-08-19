import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


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
        print('--MATCH--')
        print('file: {}'.format(match.file))
        print('line: {}'.format(match.line))
        print('text: {}'.format(match.text))


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
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, word)
        else:
            yield from search_file(full_item, word)


def search_file(filename, word):
    with open(filename, 'rb') as fin:

        line_num = 0
        for line in fin.readlines():
            line_num += 1

            line = line.decode('utf8', 'ignore').lower().strip()
            if line.find(word) >= 0:
                match = SearchResult(line=line_num, file=filename, text=line)
                yield match


if __name__ == '__main__':
    main()
