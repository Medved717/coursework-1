import os
from datetime import datetime
from idlelib.pyparse import trans
# from src.read_file import get_transactions_excel
from src.search import transactions
import pandas as pd
import os
import openpyxl
import json
from os import write
import requests
import os


def get_time():
    """Принимает время на момент использования и
    в зависимости от времени приветствует пользователя."""

    datetime_now = datetime.now()
    data_str = datetime_now.strftime('%Y-%m-%d %H:%M:%S')
    return data_str


def greeting_users(date: str) -> str:
    """Приветствие в зависимости от времени обращения."""

    if 5 <= int(date[11:13]) <= 11:
        return f'Доброе утро!'
    elif 12 <= int(date[11:13]) <= 15:
        return f'Добрый день!'
    elif 16 <= int(date[11:13]) <= 21:
        return f'Добрый вечер!'
    else:
        return f'Доброй ночи!'


def get_result_list_transaction_by_date(transactions: list[dict], input_date: str) -> list[dict]:
    """Прием даты и формирование списка словарей
    с начала месяца по полученной дате в формате от меньшей даты к большей."""

    # Приводим введенную дату в объект datetime.
    datetime_input = datetime.strptime(input_date, '%d.%m.%Y %H:%M:%S')
    # Откатываем введенную дату на начало месяца.
    datetime_beginning_of_the_month = datetime_input.replace(day=1, hour=0, minute=0, second=0)

    # Формируем условие, при котором транзации формируются исходя из периода дат.
    list_transactions = []
    for transaction in transactions:
        transaction_obj_date = datetime.strptime(transaction['Дата операции'],'%d.%m.%Y %H:%M:%S')
        if datetime_beginning_of_the_month <= transaction_obj_date <= datetime_input:
            list_transactions.append(transaction)
    return sorted(list_transactions, key=lambda  x: x['Дата операции'],   reverse=False)


def mask_card(transactions: list[dict]) -> list[dict]:
    """На вход передается список словарей с транзакциями, в том числе
    с номерами карт, после чего происходит маскировка"""
    transaction_result = []
    for transaction in transactions:
        number_card = transaction['Номер карты']
        cut_number_card = number_card[-4:]
        transaction['Номер карты'] = cut_number_card
        transaction_result.append(transaction)
    return transaction_result


def total_expenses(transactions: list[dict]) -> list:
    """Получает список словарей с транзакциями
    и возвращает объединенную сумму расходов или
    доходов в (общая сумма плюсом или минусом)."""

    # Список расходов и поступлений.
    return sum([t['Сумма операции'] for t in transactions])


def payment_amount(transactions: list[dict]) -> list[dict]:
    """Ведется подсчет топ-5 транзакций по сумме платежа (от самых больших и в обратном порядке)."""

    sorted_transaction = sorted(transactions, key=lambda x: x.get('Сумма платежа'), reverse=True)
    return sorted_transaction[:5]


def cashback(transactions: list[dict]) -> list[dict]:
    """Принимает список словарей (транзакций) высчитывает кешбек
    и возвращает список словарей с кешбеком"""

    for transaction in transactions:
        summ_cashback = transaction.get('Сумма операции') * 0.01
        if not summ_cashback:
            transaction['Кэшбэк'] = summ_cashback
        else:
            transaction['Кэшбэк'] = 0
    return transactions


def get_transactions_excel():
    """Получение файла транзакций в формате excel и перевод в список словарей."""

    file_path = os.path.join("..", "data", "operations.xlsx")
    read_file_excel = pd.read_excel(file_path)
    file_no_nan = read_file_excel.where(pd.notna(read_file_excel), "")
    exel_file_to_dict = file_no_nan.to_dict("records")
    return exel_file_to_dict

print(get_transactions_excel())


def get_csv_stocks() -> list[dict]:
    """Преобразование файла csv в объект пайтон (словарь) и выводит
    необходимые словари с наименованием компании и стоимостью акции."""

    file_path_csv = os.path.join('..', 'data', 'list_stocks.csv')
    file_csv_read = pd.read_csv(file_path_csv)
    file_to_dict = file_csv_read.to_dict('records')
    result_list_stocks = [{'stock': x['symbol'], 'price': x['price']} for x in file_to_dict if x['symbol'] in ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA']]
    return result_list_stocks


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







