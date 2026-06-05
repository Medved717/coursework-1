import os
from datetime import datetime
from idlelib.pyparse import trans
from src.read_file import get_transactions_excel


def mask_card(number_card: str) -> str:
    """На вход передается строка с номером карты,
    после чего происходит маскировка"""

    pass


def total_expenses(transactions: list[dict]) -> list:
    """Получает список словарей с транзакциями
    и возвращает объединенную сумму расходов или
    доходов в (общая сумма плюсом или минусом)."""

    # Список расходов и поступлений.
    return sum([t['Сумма операции'] for t in transactions])


def payment_amount(transactions: list[dict]) -> list[dict]:
    """Ведется подсчет топ-5 транзакций по сумме платежа (от самых больших и в обратном порядке)."""

    sorted_transaction = sorted(transactions, key=lambda x: x.get('Сумма платежа'), reverse=True)
    return sorted_transaction[:5]


def cashback(transactions: list[dict]) -> list[dict]:
    """Принимает список словарей (транзакций) высчитывает кешбек
    и возвращает список словарей с кешбеком"""

    for transaction in transactions:
        summ_cashback = transaction.get('Сумма операции') * 0.01
        if not summ_cashback:
            transaction['Кэшбэк'] = summ_cashback
        else:
            transaction['Кэшбэк'] = 0
    return transactions
