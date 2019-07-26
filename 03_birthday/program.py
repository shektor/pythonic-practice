import datetime

def print_header():
    print('BIRTHDAY APP')


def get_birthday_from_user():
    print('When were you born?')
    year = int(input('What year were you born [YYYY]: '))
    month = int(input('What month were you born [MM]: '))
    day = int(input('What day were you born [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday


def days_to_next_target_date(target, today):
    next_target = target.replace(year = today.year)
    if next_target < today:
        next_target = target.replace(year = today.year + 1)
    delta = next_target - today

    return delta.days


def print_days_to_birthday(number_of_days):
    if number_of_days == 0:
        print('It is you birthday, Happy Birthday!')
    else:
        print('It is {} days until your birthday!'.format(number_of_days))


def main():
    print_header()
    birthday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = days_to_next_target_date(birthday, today)
    print_days_to_birthday(number_of_days)


main()
