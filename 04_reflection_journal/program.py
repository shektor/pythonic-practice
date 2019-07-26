import journal


def main():
    print_header()
    run_event_loop()
    print_exit()


def print_header():
    print('REFLECTION JOURNAL')


def print_exit():
    print('Closing Journal')


def run_event_loop():
    print('What would you like to do?')

    journal_data = journal.load()

    command = None

    while command != 'x':
        command = input('[L]ist entries, [A]dd entry or E[x]it: ')
        command = command.lower().strip()

        if command == 'l':
            list_entries(journal_data)
        elif command == 'a':
            add_entry(journal_data)
        elif command != 'x':
            print('Input not recognised')

    journal.save(journal_data, 'my_reflections')


def list_entries(journal_data):
    if len(journal_data) > 0:
        print('Journal entries (most recent first):')
        journal_data = reversed(journal_data)
        for (index, entry) in enumerate(journal_data):
            print('[{}] {}'.format(index + 1, entry))
    else:
        print('Journal is empty')



def add_entry(journal_data):
    entry = input('Add an entry: ')
    journal.add(entry, journal_data)


main()
