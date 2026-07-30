import json
import logging
import os
from datetime import datetime
from os.path import abspath
from typing import Optional

import pandas as pd
from dateutil.relativedelta import relativedelta

file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
directori_path_logs = os.path.join(file_path, "logs", "log_reports.txt")

logger = logging.getLogger("reports")
file_handler = logging.FileHandler(directori_path_logs, mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s, %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def save_file_dataframe_func(func):
    def wrapper(*args, **kwargs):
        result_func = func(*args, **kwargs)
        logger.debug("Получаем результат функции из параметра.")
        func_to_dict = result_func.to_dict(orient="records")
        result = []
        for transaction in func_to_dict:
            if isinstance(transaction.get("Дата операции"), (datetime)):
                transaction["Дата операции"] = datetime.strftime(
                    transaction.get("Дата операции"), "%d.%m.%Y %H:%M:%S"
                )
                result.append(transaction)
            else:
                result.append(transaction)

        file_abspath = os.path.dirname(os.path.dirname(abspath(__file__)))
        file_path = os.path.join(file_abspath, "data", "category_pay.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False)
        return result

    logger.debug("Декоратор завершил сохранение файла и вывод в консоль сведений.")
    return wrapper


def get_transactions_in_excel_file():
    """Получаем данные из файла формата excel и переводим в формат DataFrame."""

    file_path_abs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path_exel = os.path.join(file_path_abs, "data", "operations.xlsx")
    data_frame_transactions = pd.read_excel(file_path_exel)
    logger.info("Получены данные в формате DataFrame из файла operations.xlsx.")
    return data_frame_transactions


@save_file_dataframe_func
def spending_by_category(
        transactions: pd.DataFrame, category: str, date: Optional[str] = None
) -> pd.DataFrame:
    """Функция возвращает сумму трат по заданной категории за последние три месяца"""

    if date is None:
        date_end = datetime.now()
    else:
        date_end = datetime.strptime(date, "%d.%m.%Y %H:%M:%S")

    date_start = date_end - relativedelta(months=3)

    transactions["Дата операции"] = pd.to_datetime(
        transactions["Дата операции"], format="%d.%m.%Y %H:%M:%S"
    )

    filter_transactions = transactions[
        (transactions["Категория"] == category)
        & (transactions["Дата операции"] >= date_start)
        & (transactions["Дата операции"] <= date_end)
        ]

    if filter_transactions.empty:
        logger.info("Данные не найдены!")
        print("Данная категория отсутствует в указанном периоде!")
        # Возвращаем пустой DataFrame с нужными колонками
        return pd.DataFrame(columns=["Категория", "Сумма трат за 3 месяца"])
    else:
        # Суммируем траты по категории
        total_sum = abs(filter_transactions["Сумма операции"].sum())

        # Создаем DataFrame с результатом
        result_df = pd.DataFrame([{
            "Категория": category,
            "Сумма трат за 3 месяца": round(total_sum, 2)
        }])

        logger.info(f"Сумма трат по категории '{category}': {round(total_sum, 2)}")
        return result_df
