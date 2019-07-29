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
    buy_amount = coinbase_api('buy', currency_code)

    return buy_amount


def get_sell_price(currency_code):
    sell_amount = coinbase_api('sell', currency_code)

    return sell_amount


def coinbase_api(endpoint, currency_code):
    currency_pair = 'BTC-{}'.format(currency_code)
    url = 'https://api.coinbase.com/v2/prices/{}/{}'.format(currency_pair, endpoint)
    response = requests.get(url)

    response_dictionary = response.json()
    amount = response_dictionary['data']['amount']

    return amount


def print_prices(currency_code, buy, sell):
    print('Buy 1 BTC @ {} {}'.format(buy, currency_code))
    print('Sell 1 BTC @ {} {}'.format(sell, currency_code))


if __name__ == '__main__':
    main()
