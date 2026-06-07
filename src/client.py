import json
from os import write

import requests
import os


def get_exchange_rate():
    """Прием данных по курсу валют формата json
    далее запись json-файла и вывод словаря с данными о курсе валют 'EUR' и 'USD'."""
    try:
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        file_dict = response.json()

        # Запись серверных данных в файл формата json
        # для выведения результата в случае отсутствия интернет соединения.
        file_json_path = os.path.join('..', 'data', 'exchange_rate.json')
        with open(file_json_path, 'w', encoding='utf-8') as f:
            json.dump(file_dict, f, ensure_ascii=False, indent=4)

        # Получаем суммы по USD и EUR.
        usd_rate = file_dict.get("Valute").get("USD").get("Value")
        eur_rate = file_dict.get("Valute").get("EUR").get("Value")

        result = {"currency_rates": [
            {"currency": "USD", "rate": usd_rate},
            {"currency": "EUR", "rate": eur_rate}
            ]
        }
        return result

    except requests.exceptions.RequestException:
        print('Не удалось выполнить запрос к серверу, попробуйте обратиться позже.')
        return 0.0


# Здесь будет функция по приему курсов акций.
def get_stocks():
    """Получение csv - файла со списком реализуемых акций и их стоимостями."""

    url = 'https://raw.githubusercontent.com/Ate329/top-us-stock-tickers/main/tickers/sp500.csv'
    response = requests.get(url)
    return response


def file_csv_stocks():
    """Сохраняем полученные данные по акциям в csv файл."""

    result_get_stocks = get_stocks()
    path_file_csv = os.path.join('..', 'data', 'list_stocks.csv')
    with open(path_file_csv, 'w', encoding='utf-8') as f:
        f.write(result_get_stocks.text)
    return None





