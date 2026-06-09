from datetime import datetime
import json
import pandas as pd
import os


def get_transactions_in_excel_file():
    """Получаем данные из файла формата excel и переводим в формат DataFrame."""

    file_path_exel = os.path.join('..', 'data', 'operations.xlsx')
    data_frame_transactions = pd.read_excel(file_path_exel)
    return data_frame_transactions

result = get_transactions_in_excel_file
print(get_transactions_in_excel_file())



# def spending_by_category(transactions: pd.DataFrame, category: str,
#                          date: Optional[str] = None) -> pd.DataFrame:
#     """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты),
#     если дата не передана, то берется текущая дата."""
#
#     data_transactions = pd.read_csv(transactions)
#
#     if date == None:
#         date = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')
#     else:
#         date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
#     return date







result = spending_by_category()
print(result)
date='12.12.2026 12:12:12'