import logging
from datetime import datetime
import json
from idlelib.pyparse import trans
import logging
import pandas as pd
import os

from dateutil.relativedelta import relativedelta


directori_path_logs = os.path.join('..', 'logs', 'log_reports.txt')

logger = logging.getLogger('reports')
file_handler = logging.FileHandler(directori_path_logs, mode='w', encoding='utf-8')
file_formater = logging.Formatter("%(asctime)s, %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def save_file_dataframe_func(func):
    def wrapper(*args, **kwargs):
        result_func = func(*args, **kwargs)
        logger.debug(f'Получаем результат функции из параметра.')
        func_to_dict = result_func.to_dict(orient='records')
        result = []
        for transaction in func_to_dict:
            if isinstance(transaction.get('Дата операции'), (datetime)) :
                transaction['Дата операции'] = datetime.strftime(transaction.get('Дата операции'), '%d.%m.%Y %H:%M:%S')
                result.append(transaction)
            else:
                result.append(transaction)

        file_path = os.path.join('..', 'data', 'example.json')
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)
        return result
    logger.debug(f'Декоратор завершил сохранение файла и вывод в консоль сведений.')
    return wrapper


def get_transactions_in_excel_file():
    """Получаем данные из файла формата excel и переводим в формат DataFrame."""

    file_path_exel = os.path.join('..', 'data', 'operations.xlsx')
    data_frame_transactions = pd.read_excel(file_path_exel)
    logger.info(f'Получены данные в формате DataFrame из файла operations.xlsx.')
    return data_frame_transactions


@save_file_dataframe_func
def spending_by_category(transactions: pd.DataFrame, category: str,
                         date: Optional[str] = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты),
    если дата не передана, то берется текущая дата."""

    # Получаем на входе дату или текущую дату в случае отсутствия на входе.
    if date == None:
        date_end = datetime.now()
        logger.debug(f'Получена дата, так как не введена исходная в spending_by_category.')
    else:
        date_end = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')

    # Задаем первоначальную дату поиска с разницой в 3 месяца.
    date_start = datetime.strftime(date_end - relativedelta(months=3), '%d.%m.%Y %H:%M:%S')


    # Переводим столбец "Дата операции" в формат datetime для последующего получения периода.
    transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'], format='%d.%m.%Y %H:%M:%S')

    filter_transactions = transactions[
        (transactions['Категория'] == category) &
        (transactions['Дата операции'] >= date_start) &
        (transactions['Дата операции'] <= date_end)
    ]
    logger.info(f'Получена дата, так как не введена исходная в spending_by_category.')
    return filter_transactions



