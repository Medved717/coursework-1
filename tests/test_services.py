import json

import pytest

from src.services import (get_analysis_increased_cashback,
                          get_categories_cashback)


@pytest.mark.parametrize(
    "before_transactions, after_transactions",
    [
        (
            [
                {"Дата операции": "01.05.2019 16:36:57", "Кэшбэк": 3000},
                {"Дата операции": "03.05.2019 16:36:57", "Кэшбэк": 3000},
                {"Дата операции": "10.05.2019 16:36:57", "Кэшбэк": 3000},
                {"Дата операции": "10.06.2019 16:36:57", "Кэшбэк": 3000},
            ],
            [
                {"Дата операции": "01.05.2019 16:36:57", "Кэшбэк": 3000},
                {"Дата операции": "03.05.2019 16:36:57", "Кэшбэк": 3000},
                {"Дата операции": "10.05.2019 16:36:57", "Кэшбэк": 3000},
            ],
        )
    ],
)
def test_get_analysis_increased_cashback(before_transactions, after_transactions):
    """Проверка получения списка транзакций, месяца и года,
    по которым будет производиться поиск транзакций с кэшбеком,
    после чего выводится список словарей с кэшбеком
    с периодом входных данных по дате."""

    result = get_analysis_increased_cashback(before_transactions, "05", "2019")
    assert result == after_transactions


@pytest.mark.parametrize(
    "before_transactions, after_transactions",
    [
        (
            [
                {"Категория": "Перевод", "Кэшбэк": 3000},
                {"Категория": "Магазин", "Кэшбэк": 3000},
                {"Категория": "Перевод", "Кэшбэк": 3000},
                {"Категория": "Магазин", "Кэшбэк": 3000},
                {"Нет категории": "Иное значение", "Сумма операции": 3000},
            ],
            json.dumps([{"Перевод": 6000.0}, {"Магазин": 6000.0}], ensure_ascii=False),
        )
    ],
)
def test_get_categories_cashback(before_transactions, after_transactions):
    result = get_categories_cashback(before_transactions)
    assert result == after_transactions
