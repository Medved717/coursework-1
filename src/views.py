import os
from datetime import datetime
from idlelib.pyparse import trans

from src.read_excel_file import file_path, get_transactions_excel

#
# def get_time():
#     """Принимает время на момент использования и
#     в зависимости от времени приветствует пользователя."""
#
#     datetime_now = datetime.now()
#     data_str = datetime_now.strftime('%Y-%m-%d %H:%M:%S')
#     return data_str
#
# # # Тестирование функций, не обязательная переменная.
# # result = get_time()
# # # print(result)
#
# def greeting(date: str) -> str:
#     """Приветствие в зависимости от времени обращения."""
#
#     if 5 <= int(date[11:13]) <= 11:
#         return f'Доброе утро!'
#     elif 12 <= int(date[11:13]) <= 15:
#         return f'Добрый день!'
#     elif 16 <= int(date[11:13]) <= 21:
#         return f'Добрый вечер!'
#     else:
#         return f'Доброй ночи!'
#
# # result = greeting(get_time())
# # print(result)
#
#
# def mask_card(number_card: str) -> str:
#     """На вход передается строка с номером карты,
#     после чего происходит маскировка"""
#
#     pass




     # file_path = os.path.join('vievs', 'result')

def total_expenses(transactions: list[dict]) -> list:
    """Получает список словарей с транзакциями
    и возвращает объединенную сумму расходов или доходов в зависимости от данных."""

    # Список расходов и поступлений.
    return sum([t['Сумма операции'] for t in transactions])


# result = get_transactions_excel(file_path)
# print(total_expenses(result))


def payment_amount(transactions: list[dict]) -> list[dict]:
    """Ведется подсчет топ-5 транзакций по сумме платежа (от самых больших и в обратном порядке)."""

    sorted_transaction = sorted(transactions, key=lambda x: x.get('Сумма платежа'), reverse=True)
    return sorted_transaction[:5]


# Делаю функцию ко пешбеку.
def cashback(transactions: list[dict]) -> list[dict]:
    for transaction in transactions:
        summ_cashback = transaction.get('Сумма операции') * 0.01
        if not summ_cashback:
            transaction['Кэшбэк'] = summ_cashback
        else:
            transaction['Кэшбэк'] = 0
    return transactions



