
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

    journal = []

    command = None

    while command != 'x':
        command = input('[L]ist entries, [A]dd entry or E[x]it: ')
        command = command.lower().strip()

        if command == 'l':
            list_entries(journal)
        elif command == 'a':
            add_entry(journal)
        elif command != 'x':
            print('Input not recognised')


def list_entries(journal):
    if len(journal) > 0:
        print('Journal entries (most recent first):')
        journal = reversed(journal)
        for (index, entry) in enumerate(journal):
            print('[{}] {}'.format(index + 1, entry))
    else:
        print('Journal is empty')



def add_entry(journal):
    entry = input('Add an entry: ')
    journal.append(entry)


main()
