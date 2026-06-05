import pandas as pd
import os
import openpyxl


def get_transactions_excel(transactions_file):
    """Получение файла транзакций в формате excel и перевод в список словарей."""

    file_path = os.path.join("..", "data", "operations.xlsx")
    read_file_excel = pd.read_excel(transactions_file)
    file_no_nan = read_file_excel.where(pd.notna(read_file_excel), "")
    exel_file_to_dict = file_no_nan.to_dict("records")
    return exel_file_to_dict


def get_csv_stocks() -> list[dict]:
    """Преобразование файла csv в объект пайтон (словарь) и выводит
    необходимые словари с наименованием компании и стоимостью акции."""

    file_path_csv = os.path.join('..', 'data', 'list_stocks.csv')
    file_csv_read = pd.read_csv(file_path_csv)
    file_to_dict = file_csv_read.to_dict('records')
    result_list_stocks = [{'stock': x['symbol'], 'price': x['price']} for x in file_to_dict if x['symbol'] in ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA']]
    return result_list_stocks




