import pytest
from src.date_search import get_result_list_transaction_by_date

@pytest.mark.parametrize(
    'transactions_before, transactions_after', [
        ([{'Дата операции': '01.07.2018 12:49:53'},
        {'Дата операции': '12.07.2018 16:49:53'},
        {'Дата операции': '02.07.2018 12:49:53'}],

        [{'Дата операции': '01.07.2018 12:49:53'},
        {'Дата операции': '02.07.2018 12:49:53'},
        {'Дата операции': '12.07.2018 16:49:53'}])
    ]
)

def test_get_result_list_transaction_by_date(transactions_before, transactions_after):
    input_date = '30.07.2018 12:49:53'
    result = get_result_list_transaction_by_date(transactions_before, input_date)
    assert result == transactions_after