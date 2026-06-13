import datetime
import os
from unittest.mock import Mock, mock_open, patch

import pytest
import requests

from src.views import (file_csv_stocks, get_csv_stocks, get_exchange_rate,
                       get_result_list_transaction_by_date, get_stocks,
                       get_time, get_transactions_excel, greeting_users,
                       mask_card)


@patch("src.views.requests.get")
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
                "Previous": 72.5597,
            },
            "EUR": {
                "ID": "R01239",
                "NumCode": "978",
                "CharCode": "EUR",
                "Nominal": 1,
                "Name": "Евро",
                "Value": 85.1243,
                "Previous": 84.6096,
            },
        },
    }
    result = get_exchange_rate()
    assert result == {
        "currency_rates": [
            {"currency": "USD", "rate": 73.3436},
            {"currency": "EUR", "rate": 85.1243},
        ]
    }


@patch("src.views.requests.get")
def test_get_exchange_rate_no_internet(mock_get):
    """Проверка работы функции при отсутствии интернета"""

    mock_get.side_effect = requests.exceptions.RequestException(
        "Нет интернет соединения!"
    )
    result = get_exchange_rate()
    assert result == 0.0


@patch("src.views.requests.get")
def test_get_stocks(mock_get):
    """Мокаем requests.get."""

    fake_response = Mock()
    fake_response.text = "Вернулся текст."
    mock_get.return_value = fake_response
    get_stocks()
    mock_get.assert_called_once()


@patch("src.views.get_stocks")
@patch("src.views.open", new_callable=mock_open)
@patch("src.views.os.path.join")
def test_file_csv_stocks(mock_join, fake_response, mock_get_stocks):
    """Проверка использования пути сохранения."""

    mock_get_stocks.return_value.txt = "Текст из интернета."
    mock_join.return_value = "Строка пути!"
    fake_response.return_value.txt = "Фальшивое сохранение."
    file_csv_stocks()
    file_path_csv_stocks = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mock_join.assert_called_once_with(file_path_csv_stocks, "data", "list_stocks.csv")


@patch("src.views.pd.read_excel")
@patch("src.views.os.path.join")
def test_get_transactions_excel(mock_os_path_join, mock_pd_read_excel):
    """Проверяем вывод списка словарей."""

    mock_os_path_join.return_value = "Путь к файлу"
    mock_df = Mock()
    mock_pd_read_excel.return_value = mock_df
    mock_were = Mock()
    mock_df.where.return_value = mock_were
    mock_were.to_dict.return_value = [{"id": 1, "name": "test"}]
    result = get_transactions_excel()
    assert result == [{"id": 1, "name": "test"}]


@patch("src.views.pd.read_csv")
@patch("src.views.os.path.join")
def test_get_csv_stocks(
    mock_os_path_join, mock_pd_read_csv, stock_list_data, stock_list_filter
):
    """Мокаем join и pd.read_csv, после чего выводим список словарей."""

    mock_os_path_join.return_value = "Текст пути к файлу."
    mock_result_read_csv = Mock()
    mock_pd_read_csv.return_value = mock_result_read_csv
    mock_result_read_csv.to_dict.return_value = stock_list_data
    result = get_csv_stocks()
    assert result == stock_list_filter


@patch("src.views.pd.read_csv")
@patch("src.views.os.path.join")
def test_get_csv_stocks_path(mock_join, mock_read, stock_list_data, stock_list_filter):
    """Тестирование использования csv файла и вывода необходимых словарей."""

    mock_join.return_value = "Строка с путем к файлу."
    fake_read_csv = Mock()
    mock_read.return_value = fake_read_csv
    fake_read_csv.to_dict.return_value = stock_list_data
    result = get_csv_stocks()
    assert result == stock_list_filter


def test_mask_card(operations_data_card_befor, operations_data_card_after):
    """Тестируем маскировку карты"""

    result = mask_card(operations_data_card_befor)
    assert result == operations_data_card_after


@patch("src.views.datetime")
def test_get_time(mock_datetime):
    """Тестирование методом mock по настоящему времени с подменой."""

    mock_datetime.now.return_value = datetime.datetime(2026, 6, 3, 10, 28, 4)
    result = get_time()
    assert result == "2026-06-03 10:28:04"


@patch("src.views.datetime")
def test_greeting_users_morning(mock_get_time):
    """Тест по выводу: 'Доброе утро'"""

    mock_get_time.return_value = "2026-06-03 10:28:04"
    result = greeting_users(mock_get_time.return_value)
    assert result == "Доброе утро!"


@patch("src.views.datetime")
def test_greeting_users_day(mock_get_time):
    """Тест по выводу: 'Добрый день!'"""

    mock_get_time.return_value = "2026-06-03 15:28:04"
    result = greeting_users(mock_get_time.return_value)
    assert result == "Добрый день!"


@patch("src.views.datetime")
def test_greeting_users_evening(mock_get_time):
    """Тест по выводу: 'Добрый вечер!'"""

    mock_get_time.return_value = "2026-06-03 20:28:04"
    result = greeting_users(mock_get_time.return_value)
    assert result == "Добрый вечер!"


@patch("src.views.datetime")
def test_greeting_users_night(mock_get_time):
    """Тест по выводу: 'Доброй ночи!'"""

    mock_get_time.return_value = "2026-06-03 03:28:04"
    result = greeting_users(mock_get_time.return_value)
    assert result == "Доброй ночи!"


@pytest.mark.parametrize(
    "transactions_before, transactions_after",
    [
        (
            [
                {"Дата операции": "01.07.2018 12:49:53"},
                {"Дата операции": "12.07.2018 16:49:53"},
                {"Дата операции": "02.07.2018 12:49:53"},
            ],
            [
                {"Дата операции": "01.07.2018 12:49:53"},
                {"Дата операции": "02.07.2018 12:49:53"},
                {"Дата операции": "12.07.2018 16:49:53"},
            ],
        )
    ],
)
def test_get_result_list_transaction_by_date(transactions_before, transactions_after):
    input_date = "30.07.2018 12:49:53"
    result = get_result_list_transaction_by_date(transactions_before, input_date)
    assert result == transactions_after
