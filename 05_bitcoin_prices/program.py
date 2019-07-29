import requests


def main():
    print_header()
    currency_code = input_currency_code()
    buy_price = get_buy_price(currency_code)
    print_prices(currency_code, buy_price)


def print_header():
    print('BITCOIN PRICES')


def input_currency_code():
    currency_code = input('What currency would you like the prices in: ')
    return currency_code


def get_buy_price(currency_code):
    currency_pair = 'BTC-{}'.format(currency_code)
    url = 'https://api.coinbase.com/v2/prices/{}/buy'.format(currency_pair)
    response = requests.get(url)

    response_dictionary = response.json()
    amount = response_dictionary['data']['amount']

    return amount


def print_prices(currency_code, buy):
    print('Buy 1 BTC @ {} {}'.format(buy, currency_code))


if __name__ == '__main__':
    main()
