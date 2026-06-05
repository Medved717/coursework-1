import os
from datetime import datetime
from idlelib.pyparse import trans
from src.read_file import get_transactions_excel

from src.search import transactions


def mask_card(transactions: list[dict]) -> list[dict]:
    """На вход передается список словарей с транзакциями, в том числе
    с номерами карт, после чего происходит маскировка"""
    transaction_result = []
    for transaction in transactions:
        number_card = transaction['Номер карты']
        cut_number_card = number_card[-4:]
        transaction['Номер карты'] = cut_number_card
        transaction_result.append(transaction)
    return transaction_result



result = mask_card(transactions)
print(result)







#
#
#
#
#
#
# def total_expenses(transactions: list[dict]) -> list:
#     """Получает список словарей с транзакциями
#     и возвращает объединенную сумму расходов или
#     доходов в (общая сумма плюсом или минусом)."""
#
#     # Список расходов и поступлений.
#     return sum([t['Сумма операции'] for t in transactions])
#
#
# def payment_amount(transactions: list[dict]) -> list[dict]:
#     """Ведется подсчет топ-5 транзакций по сумме платежа (от самых больших и в обратном порядке)."""
#
#     sorted_transaction = sorted(transactions, key=lambda x: x.get('Сумма платежа'), reverse=True)
#     return sorted_transaction[:5]
#
#
# def cashback(transactions: list[dict]) -> list[dict]:
#     """Принимает список словарей (транзакций) высчитывает кешбек
#     и возвращает список словарей с кешбеком"""
#
#     for transaction in transactions:
#         summ_cashback = transaction.get('Сумма операции') * 0.01
#         if not summ_cashback:
#             transaction['Кэшбэк'] = summ_cashback
#         else:
#             transaction['Кэшбэк'] = 0
#     return transactions
