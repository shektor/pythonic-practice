import os
import csv
import statistics
from transaction import Transaction


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

    transactions = []
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            transaction = Transaction.create_from_dict(row)
            transactions.append(transaction)

    return transactions


def query_data(data):
    data.sort(key=lambda transaction: transaction.price)

    high_transaction = data[-1]
    print('Most expensive house: ${:,}'.format(high_transaction.price))

    low_transaction = data[0]
    print('Least expensive house: ${:,}'.format(low_transaction.price))

    prices = (
        transaction.price
        for transaction in data
    )
    average_price = statistics.mean(prices)
    print('Average house price: ${:,}'.format(int(average_price)))

    two_bed_prices = (
        transaction.price
        for transaction in data
        if transaction.beds == 2
    )
    average_2bed_price = statistics.mean(two_bed_prices)
    print('Average 2 bed house price: ${:,}'.format(int(average_2bed_price)))


if __name__ == '__main__':
    main()
