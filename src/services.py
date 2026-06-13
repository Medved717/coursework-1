import json
from datetime import datetime
import logging
import os

file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path_log_file = os.path.join(file_path, 'logs', 'log_services.txt')

logger = logging.getLogger('services')
file_handler = logging.FileHandler(file_path_log_file, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s, %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)



def get_analysis_increased_cashback(transactions: list[dict], month: str, year: str) -> list[dict]:
    """Получаем список транзакций за период входных данных месяц, год,
    по которым выводим список транзакций с кэшбэком."""

    # Приводим входные данные по дате в формат datetime с целью последующего сравнения.
    date_addition = month + '.' + year
    input_date = datetime.strptime(date_addition, '%m.%Y')
    logger.debug(f'Объединена дата в функции get_analysis_increased_cashback')

    # Создаем итерацию и проходим по транзакциям,
    # после чего выбираем траназкции в периоде входных данных и вывод списка словарей.
    list_cashback_tranansactions = []
    for transaction in transactions:
        transaction_strp = datetime.strptime(transaction["Дата операции"], '%d.%m.%Y %H:%M:%S')
        if (transaction_strp.strftime('%m.%Y') == input_date.strftime('%m.%Y') and transaction["Кэшбэк"] != ''
                and '-' not in str(transaction["Кэшбэк"])):
            logger.debug(f'Пройдено условие по Кэшбэку')
            list_cashback_tranansactions.append(transaction)
            logger.info(f'Получен список словарей со списком транзакций с кэшбэком.')
    return list_cashback_tranansactions


def get_categories_cashback(transactions):
    """Получение списка транзакций и вывод списка словарей в формате json,
    в котором будут категории и сумма кэшбэка."""

    list_transactions = []
    for transaction in transactions:
        if transaction.get("Категория") and transaction.get("Кэшбэк") != None:
            categories_cashback = {transaction["Категория"]: transaction["Кэшбэк"]}
            list_transactions.append(categories_cashback)
            logger.debug(f'Пройдено условие по категориям и кэшбэку в функции get_categories_cashback.')

    dict_categories = {}
    for category in list_transactions:
        for key, value in category.items():

            if key in dict_categories:
                dict_categories[key] += float(value)
            else:
                dict_categories[key] = float(value)

    result_list = []
    for key, value in dict_categories.items():
        result_list.append({key: round(value, 2)})

    return json.dumps(result_list, ensure_ascii=False)
logger.debug(f'Получен json - файл с транзакциями  кэшбеком в функции get_categories_cashback.')


