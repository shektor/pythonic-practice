import os


def load(name):
    filename = get_full_path(name)
    print('Opening journal {}'.format(filename))

    data = []

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for entry in file.readlines():
                data.append(entry.rstrip())

    return data


def save(journal, name):
    filename = get_full_path(name)

    print('Saving journal to {}'.format(filename))

    with open(filename, 'w') as file:
        for entry in journal:
            file.write(entry + '\n')


def add(text, journal):
    journal.append(text)


def get_full_path(name):
    relative_path = os.path.join('.', 'journals', name + '.jrl')
    filename = os.path.abspath(relative_path)

    return filename
