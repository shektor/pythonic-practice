import os
import csv


def main():
    print_header()
    filename = get_data_file()
    transactions = load_file(filename)
    query_data(transactions)


def print_header():
    print('Real Estate Data Mining')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'data', 'transactions.csv')
    return file_path


def load_file(filename):
    print('Loading data from: {}'.format(filename))

    data = []
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            print(row)
            data.append(row)

    return data


def query_data(data):
    for row in data:
        print(row)


if __name__ == '__main__':
    main()
