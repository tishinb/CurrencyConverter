import requests
import config

usd_currency = 'USD'
rub_currency = 'RUB'
amount = float
url = 'https://v6.exchangerate-api.com/v6/{}/pair/{}/{}'

def converter():
    select_currency = int(input(f'Введите 1, для конвертации {usd_currency} в {rub_currency} или 2, для конвертации {rub_currency} в {usd_currency}: '))
    if select_currency == 1:
        currency_amount = float(input(f'Введите количество {usd_currency}: '))
        response = requests.get(url.format(config.key, usd_currency, rub_currency))
        result = response.json()
        if response.status_code == 200:
            rate = result['conversion_rate']
            converted_amount = currency_amount * rate
            print(f'{currency_amount} {usd_currency} = {converted_amount} {rub_currency}')
        else:
            print('Ошибка доступа к API!')
    elif select_currency == 2:
        currency_amount = float(input(f'Введите количество {rub_currency}: '))
        response = requests.get(url.format(config.key, rub_currency, usd_currency))
        result = response.json()
        if response.status_code == 200:
            rate = result['conversion_rate']
            converted_amount = currency_amount * rate
            print(f'{currency_amount} {rub_currency} = {converted_amount} {usd_currency}')
        else:
            print('Ошибка доступа к API!')
converter()
