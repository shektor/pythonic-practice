import os


def load():
    return []


def save(journal, name):
    relative_path = os.path.join('./journals/', name + '.jrl')
    filename = os.path.abspath(relative_path)

    print('Saving journal to {}'.format(filename))

    file = open(filename, 'w')

    for entry in journal:
        file.write(entry + '\n')

    file.close()


def add(text, journal):
    journal.append(text)
