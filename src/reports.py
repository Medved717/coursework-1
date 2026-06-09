# from datetime import datetime
# import json
# import pandas as pd
# import os
# from dateutil.relativedelta import relativedelta
#
# from src.transactions import transactions
#
#
# def get_transactions_in_excel_file():
#     """Получаем данные из файла формата excel и переводим в формат DataFrame."""
#
#     file_path_exel = os.path.join('..', 'data', 'operations.xlsx')
#     data_frame_transactions = pd.read_excel(file_path_exel)
#     return data_frame_transactions
#
# # result = get_transactions_in_excel_file
# # print(get_transactions_in_excel_file())
#
#
#
# def spending_by_category(transactions: pd.DataFrame, category: str,
#                          date: Optional[str] = None) -> pd.DataFrame:
#     """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты),
#     если дата не передана, то берется текущая дата."""
#
#     # Получаем на входе дату или текущую дату в случае отсутствия на входе.
#     if date == None:
#         date_now = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')
#     else:
#         date_now = datetime.strftime(date, '%d.%m.%Y %H:%M:%S')
#
#     # Задаем первоначальную дату поиска с разницой в 3 месяца.
#     period_time = datetime.strftime(date_now - relativedelta(months=3), '%d.%m.%Y %H:%M:%S')
#
#
#
#     category_period = transactions[category][6020]
#     date_operations = transactions['Дата операции']
#
#     transactions_filter = transactions[transactions[category],[transactions['Дата операции'] >= period_time,  transactions['Дата операции'] <= date_now]]
#     return transactions_filter
#
#
#
# result = spending_by_category(transactions=get_transactions_in_excel_file(), category='Категория',  date='12.01.2018 12:12:12')
# print(result)
# date='12.12.2026 12:12:12'


# Разобрать!!!!!!!!!!!!!!!!!!!!!!

from datetime import datetime
import pandas as pd
import os
from dateutil.relativedelta import relativedelta
from typing import Optional


def get_transactions_in_excel_file():
    """Получаем данные из файла формата excel и переводим в формат DataFrame."""
    file_path_exel = os.path.join('..', 'data', 'operations.xlsx')
    data_frame_transactions = pd.read_excel(file_path_exel)
    return data_frame_transactions


def spending_by_category(transactions: pd.DataFrame, category: str,
                         date: Optional[str] = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца"""

    # 1. Определяем конечную дату
    if date is None:
        end_date = datetime.now()
    else:
        end_date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')

    # 2. Вычисляем начальную дату (3 месяца назад)
    start_date = end_date - relativedelta(months=3)

    # 3. Преобразуем колонку с датами (указываем полный формат с временем)
    transactions['Дата операции'] = pd.to_datetime(
        transactions['Дата операции'],
        format='%d.%m.%Y %H:%M:%S'  # ✅ Теперь с временем
    )

    # 4. Фильтруем по категории и периоду дат
    transactions_filter = transactions[
        (transactions['Категория'] == category) &
        (transactions['Дата операции'] >= start_date) &
        (transactions['Дата операции'] <= end_date)
        ]

    return transactions_filter


# Вызов функции
result = spending_by_category(
    transactions=get_transactions_in_excel_file(),
    category='Связь',
    date='12.07.2019 12:12:12'
)

print(result)
