import pytest
from unittest.mock import Mock, patch

from src.services import get_analysis_increased_cashback


@pytest.mark.parametrize(
    'before_transactions, after_transactions', [
        ([{"Дата операции": "01.05.2019 16:36:57", "Кэшбэк": 3000},
          {"Дата операции": "03.05.2019 16:36:57", "Кэшбэк": 3000},
          {"Дата операции": "10.05.2019 16:36:57", "Кэшбэк": 3000},
          {"Дата операции": "10.06.2019 16:36:57", "Кэшбэк": 3000}],

         [{"Дата операции": "01.05.2019 16:36:57", "Кэшбэк": 3000},
          {"Дата операции": "03.05.2019 16:36:57", "Кэшбэк": 3000},
          {"Дата операции": "10.05.2019 16:36:57", "Кэшбэк": 3000}])
    ]
)
def test_get_analysis_increased_cashback(before_transactions, after_transactions):
    """Проверка получения списка транзакций, месяца и года,
    по которым будет производиться поиск транзакций с кэшбеком,
    после чего выводится список словарей с кэшбеком
    с периодом входных данных по дате."""

    result = get_analysis_increased_cashback(before_transactions, '05', '2019')
    assert result == after_transactions