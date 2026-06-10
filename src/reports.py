from datetime import datetime
import json
from idlelib.pyparse import trans

import pandas as pd
import os

from dateutil.relativedelta import relativedelta



# Используется для тестов, удалить!!!!!!!!!!!!!!!!!!!!!
from src.transactions import transactions



# Прописать ЛОГИРОАВНИЕ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def reports_file(func):
    def wrapper(*args, **kwargs):
        result_func = func(*args, **kwargs)
        result_func = result_func.to_dict(orient='records')
        datetime_str_list_transactions = []
        for transaction in result_func:
            for key, value in transaction.items():
                if key == 'Дата операции':
                    value = datetime.strftime(value, '%d.%m.%Y %H:%M:%S')
                    transaction[key] = value
            datetime_str_list_transactions.append(transaction)

        file_path = os.path.join('..', 'data', 'result_reports.json')
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(datetime_str_list_transactions, f, ensure_ascii=False)
        return datetime_str_list_transactions
    return wrapper








def get_transactions_in_excel_file():
    """Получаем данные из файла формата excel и переводим в формат DataFrame."""

    file_path_exel = os.path.join('..', 'data', 'operations.xlsx')
    data_frame_transactions = pd.read_excel(file_path_exel)
    return data_frame_transactions


@reports_file
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
    return filter_transactions



# Это проверка, удалить!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
result = spending_by_category(get_transactions_in_excel_file(),  category='Связь', date='22.02.2018 22:55:12')
print(result)


