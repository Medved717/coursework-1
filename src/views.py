import logging
import os
from datetime import datetime
from idlelib.pyparse import trans
import pandas as pd
import os
import openpyxl
import json
from os import write
import requests
import os


file_path_log_file = os.path.join('logs', 'log_views.txt')

logger = logging.getLogger('views')
file_handler = logging.FileHandler(file_path_log_file, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s, %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)



def get_time():
    """Принимает время на момент использования и
    в зависимости от времени приветствует пользователя."""

    datetime_now = datetime.now()
    data_str = datetime_now.strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f'Получена дата в функции get_time.')
    return data_str


def greeting_users(date: str) -> str:
    """Приветствие в зависимости от времени обращения."""

    if 5 <= int(date[11:13]) <= 11:
        logger.debug(f'Получено приветствие.')
        return f'Доброе утро!'
    elif 12 <= int(date[11:13]) <= 15:
        logger.debug(f'Получено приветствие.')
        return f'Добрый день!'
    elif 16 <= int(date[11:13]) <= 21:
        logger.debug(f'Получено приветствие.')
        return f'Добрый вечер!'
    else:
        logger.debug(f'Получено приветствие.')
        return f'Доброй ночи!'


def get_transactions_excel():
    """Получение файла транзакций в формате excel и перевод в список словарей."""

    file_path = os.path.join("data", "operations.xlsx")
    read_file_excel = pd.read_excel(file_path)
    file_no_nan = read_file_excel.where(pd.notna(read_file_excel), "")
    exel_file_to_dict = file_no_nan.to_dict("records")
    logger.info(f'Получен файл транзакций в формате excel и переведен в список словарей в функции \n'
                f'get_transactions_excel')
    return exel_file_to_dict


def mask_card(transactions: list[dict]) -> list[dict]:
    """На вход передается список словарей с транзакциями, в том числе
    с номерами карт, после чего происходит маскировка"""
    transaction_result = []
    for transaction in transactions:
        number_card = transaction['Номер карты']
        cut_number_card = number_card[-4:]
        transaction['Номер карты'] = cut_number_card
        transaction_result.append(transaction)
    logger.info(f'Получена маскировка карт в списке словарей с транзакциями в функции mask_card.')
    return transaction_result


def cashback(transactions: list[dict]) -> list[dict]:
    """Принимает список словарей (транзакций) высчитывает кэшбэк
    и возвращает список словарей с кэшбэком"""

    for transaction in transactions:
        summ_cashback = transaction.get('Сумма операции') * 0.01
        if float(transaction['Сумма операции']) < 0:
            transaction['Кэшбэк'] = round(abs(summ_cashback), 2)
        else:
            transaction['Кэшбэк'] = '0'
    logger.info(f'Посчитан кэшбек в списке транзакций в функции cashback.')
    return transactions


def get_result_list_transaction_by_date(transactions: list[dict], input_date: str) -> list[dict]:
    """Прием даты и формирование списка словарей (транзакций)
    с начала месяца по полученной дате в формате от меньшей даты к большей."""

    # Приводим введенную дату в объект datetime.
    datetime_input = datetime.strptime(input_date, '%d.%m.%Y %H:%M:%S')
    # Откатываем введенную дату на начало месяца.
    datetime_beginning_of_the_month = datetime_input.replace(day=1, hour=0, minute=0, second=0)
    logger.debug(f'Получена начальния дата в функции get_result_list_transaction_by_date.')

    # Формируем условие, при котором транзации формируются исходя из периода дат.
    list_transactions = []
    for transaction in transactions:
        transaction_obj_date = datetime.strptime(transaction['Дата операции'],'%d.%m.%Y %H:%M:%S')
        if datetime_beginning_of_the_month <= transaction_obj_date <= datetime_input:
            list_transactions.append(transaction)
    logger.info(f'Получен список словарей с начала месяца по полученной дате в формате от меньшей даты к большей\n'
                f'в функции get_result_list_transaction_by_date.')
    return sorted(list_transactions, key=lambda  x: x['Дата операции'],   reverse=False)


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


def get_stocks():
    """Получение csv - файла со списком реализуемых акций и их стоимостями."""

    url = 'https://raw.githubusercontent.com/Ate329/top-us-stock-tickers/main/tickers/sp500.csv'
    response = requests.get(url)
    logger.info(f'Получен csv - файл со списком реализуемых акций и их стоимостями в функции get_stocks.')
    return response


def get_csv_stocks() -> list[dict]:
    """Преобразование файла csv в объект пайтон (словарь) и выводит
    необходимые словари с наименованием компании и стоимостью акции."""

    file_path_csv = os.path.join('data', 'list_stocks.csv')
    file_csv_read = pd.read_csv(file_path_csv)
    file_to_dict = file_csv_read.to_dict('records')
    result_list_stocks = [{'stock': x['symbol'], 'price': x['price']} for x in file_to_dict if x['symbol']
                          in ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA']]
    logger.info(f'Преобразован файл csv в объект пайтон (словарь) и выведены необходимые словари \n'
                f' с наименованием компании и стоимостью акции. в функции get_csv_stocks')
    return result_list_stocks


def file_csv_stocks():
    """Сохраняем полученные данные по акциям в csv файл."""

    result_get_stocks = get_stocks()
    path_file_csv = os.path.join('data', 'list_stocks.csv')
    with open(path_file_csv, 'w', encoding='utf-8') as f:
        f.write(result_get_stocks.text)
        logger.info(f'Данные по акциям сохранены (file_csv_stocks).')
    return None


def get_exchange_rate():
    """Прием данных по курсу валют формата json
    далее запись json-файла и вывод словаря с данными о курсе валют 'EUR' и 'USD'."""
    try:
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        file_dict = response.json()

        # Запись серверных данных в файл формата json
        # для выведения результата в случае отсутствия интернет соединения.
        file_json_path = os.path.join('data', 'exchange_rate.json')
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
        logger.info(f'Осуществлен Прием данных по курсу валют формата json, осуществлен \n'
                    f'вывод словаря с данными о курсе валют "EUR" и "USD". в функции get_exchange_rate.')
        return result

    except requests.exceptions.RequestException:
        print('Не удалось выполнить запрос к серверу, попробуйте обратиться позже.')
        logger.error(f'Ошибка к запросу сервера в функции get_exchange_rate')
        return 0.0
