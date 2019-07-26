
def main():
    print_header()
    run_event_loop()
    print_exit()


def print_header():
    print('REFLECTION JOURNAL')


def print_exit():
    print('Closing Journal.')


def run_event_loop():
    print('What would you like to do?')

    command = None

    while command != 'x':
        command = input('[L]ist entries, [A]dd entry or E[x]it: ')
        command = command.lower().strip()

        if command == 'l':
            list_entries()
        elif command == 'a':
            add_entry()
        elif command != 'x':
            print('Input not recognised')


def list_entries():
    pass


def add_entry():
    pass


main()
