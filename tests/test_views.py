import os
from msvcrt import putch

import pytest
import requests
from unittest.mock import patch, MagicMock, Mock
from src.client import get_exchange_rate, get_stocks, file_csv_stocks


@patch('src.client.requests.get')
def test_get_exchange_rate(mock_get):
    """Проверяет работу с полученными данными сервара по валютам."""

    mock_get.return_value.json.return_value = {
    "Date": "2026-06-04T11:30:00+03:00",
    "PreviousDate": "2026-06-03T11:30:00+03:00",
    "PreviousURL": "//www.cbr-xml-daily.ru/archive/2026/06/03/daily_json.js",
    "Timestamp": "2026-06-04T14:00:00+03:00",
    "Valute": {
        "USD": {
            "ID": "R01235",
            "NumCode": "840",
            "CharCode": "USD",
            "Nominal": 1,
            "Name": "Доллар США",
            "Value": 73.3436,
            "Previous": 72.5597
        },
        "EUR": {
            "ID": "R01239",
            "NumCode": "978",
            "CharCode": "EUR",
            "Nominal": 1,
            "Name": "Евро",
            "Value": 85.1243,
            "Previous": 84.6096
        }
    }
}
    result = get_exchange_rate()
    assert result == {'currency_rates': [{'currency': 'USD', 'rate': 73.3436},
                                         {'currency': 'EUR', 'rate': 85.1243}]}


@patch('src.client.requests.get')
def test_get_exchange_rate_no_internet(mock_get):
    """Проверка работы функции при отсутствии интернета"""

    mock_get.side_effect = requests.exceptions.RequestException('Нет интернет соединения!')
    result = get_exchange_rate()
    assert result == 0.0


@patch('src.client.requests.get')
def test_get_stocks(mock_get):
    """Мокаем requests.get."""

    fake_response = Mock()
    fake_response.text = 'Вернулся текст.'
    mock_get.return_value = fake_response
    result = get_stocks()
    mock_get.assert_called_once()


@patch('src.client.os.path.join')
def test_file_csv_stocks(mock_join):
    """Проверка использования пути сохранения."""

    file_csv_stocks()
    mock_join.assert_called_once_with('..', 'data', 'list_stocks.csv')


