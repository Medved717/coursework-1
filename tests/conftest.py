import pandas as pd
import pytest


@pytest.fixture
def stock_list_data():
    "Фикстура со списком отсоритрованных акциа."

    return [
        {'symbol': 'AAPL', 'price': 310.26, 'volume': 50836952, 'industry': 'Technology'},
        {'symbol': 'AMZN', 'price': 130.50, 'volume': 30000000, 'industry': 'Consumer Cyclical'},
        {'symbol': 'GOOGL', 'price': 140.75, 'volume': 25000000, 'industry': 'Technology'},
        {'symbol': 'MSFT', 'price': 330.45, 'volume': 20000000, 'industry': 'Technology'},
        {'symbol': 'TSLA', 'price': 423.70, 'volume': 45000000, 'industry': 'Automotive'},
        {'symbol': 'NVDA', 'price': 214.75, 'volume': 160910801, 'industry': 'Technology'},
    ]


@pytest.fixture()
def stock_list_filter():
    """Фикстура возвращает отфилтрованный список акций."""

    return [
        {'stock': 'AAPL', 'price': 310.26},
        {'stock': 'AMZN', 'price': 130.50},
        {'stock': 'GOOGL', 'price': 140.75},
        {'stock': 'MSFT', 'price': 330.45},
        {'stock': 'TSLA', 'price': 423.70},
    ]


@pytest.fixture()
def operations_data_card_befor():
    return [{'Дата операции': '01.01.2018 12:49:53', 'Дата платежа': '01.01.2018', 'Номер карты': '*7197',
             'Статус': 'OK', 'Сумма операции': -3000.0, 'Валюта операции': 'RUB', 'Сумма платежа': -3000.0,
             'Валюта платежа': 'RUB', 'Кэшбэк': '', 'Категория': 'Переводы', 'MCC': '',
             'Описание': 'Линзомат ТЦ Юность', 'Бонусы (включая кэшбэк)': 0, 'Округление на инвесткопилку': 0,
             'Сумма операции с округлением': 3000.0}]


@pytest.fixture()
def operations_data_card_after():
    return [{'Дата операции': '01.01.2018 12:49:53', 'Дата платежа': '01.01.2018', 'Номер карты': '7197',
             'Статус': 'OK', 'Сумма операции': -3000.0, 'Валюта операции': 'RUB', 'Сумма платежа': -3000.0,
             'Валюта платежа': 'RUB', 'Кэшбэк': '', 'Категория': 'Переводы', 'MCC': '',
             'Описание': 'Линзомат ТЦ Юность', 'Бонусы (включая кэшбэк)': 0, 'Округление на инвесткопилку': 0,
             'Сумма операции с округлением': 3000.0}]


@pytest.fixture()
def operations_date():
    return [{'Дата операции': '01.07.2018 12:49:53'},
            {'Дата операции': '12.07.2018 16:49:53'},
            {'Дата операции': '02.07.2018 12:49:53'}]


@pytest.fixture()
def operations_dataframe():
    return pd.DataFrame({
        'Дата операции': ['01.07.2018 12:49:53',
                          '12.07.2018 16:49:53',
                          '02.07.2018 12:49:53'],
        'Категория': ['Связь',
            'Различные товары',
            'Транспорт']
    })