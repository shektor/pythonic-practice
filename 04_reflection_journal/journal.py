import os


def load():
    return []


def save(journal, name):
    relative_path = os.path.join('.', 'journals', name + '.jrl')
    filename = os.path.abspath(relative_path)

    print('Saving journal to {}'.format(filename))

    with open(filename, 'w') as file:
        for entry in journal:
            file.write(entry + '\n')


def add(text, journal):
    journal.append(text)
