import requests


def main():
    print_header()
    currency_code = input_currency_code()
    buy_price = get_buy_price(currency_code)
    sell_price = get_sell_price(currency_code)

    print_prices(currency_code, buy_price, sell_price)


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
    buy_amount = response_dictionary['data']['amount']

    return buy_amount


def get_sell_price(currency_code):
    currency_pair = 'BTC-{}'.format(currency_code)
    url = 'https://api.coinbase.com/v2/prices/{}/sell'.format(currency_pair)
    response = requests.get(url)

    response_dictionary = response.json()
    sell_amount = response_dictionary['data']['amount']

    return sell_amount


def print_prices(currency_code, buy, sell):
    print('Buy 1 BTC @ {} {}'.format(buy, currency_code))
    print('Sell 1 BTC @ {} {}'.format(sell, currency_code))


if __name__ == '__main__':
    main()
