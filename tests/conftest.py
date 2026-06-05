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


