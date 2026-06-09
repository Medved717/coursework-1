from datetime import datetime
import json
from idlelib.pyparse import trans

import pandas as pd
import os
from dateutil.relativedelta import relativedelta

from src.transactions import transactions


def get_transactions_in_excel_file():
    """Получаем данные из файла формата excel и переводим в формат DataFrame."""

    file_path_exel = os.path.join('..', 'data', 'operations.xlsx')
    data_frame_transactions = pd.read_excel(file_path_exel)
    return data_frame_transactions


def spending_by_category(transactions: pd.DataFrame, category: str,
                         date: Optional[str] = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты),
    если дата не передана, то берется текущая дата."""

    # Получаем на входе дату или текущую дату в случае отсутствия на входе.
    if date == None:
        date_end = datetime.now()
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
    return filter_transactions[['Категория', 'Дата операции']]





