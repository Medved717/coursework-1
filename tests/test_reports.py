from unittest.mock import patch

import pandas as pd
import pytest

from src.reports import get_transactions_in_excel_file, spending_by_category


@patch("src.reports.pd.read_excel")
@patch("src.reports.os.path.join")
def test_get_transactions_in_excel_file(
    mock_join, mock_read_excel, operations_dataframe
):
    mock_join.return_value = "Путь к файлу"
    mock_read_excel.return_value = operations_dataframe
    result = get_transactions_in_excel_file()
    assert result.to_dict() == operations_dataframe.to_dict()


@pytest.mark.parametrize(
    "transactions_before, transactions_after",
    [
        (
            pd.DataFrame(
                {
                    "Дата операции": [
                        "01.07.2018 12:49:53",
                        "11.07.2018 12:48:53",
                        "12.07.2018 16:49:53",
                        "02.07.2018 12:49:53",
                    ],
                    "Категория": ["Связь", "Связь", "Различные товары", "Транспорт"],
                }
            ),
            pd.DataFrame(
                {
                    "Дата операции": ["01.07.2018 12:49:53", "11.07.2018 12:48:53"],
                    "Категория": ["Связь", "Связь"],
                }
            ),
        )
    ],
)
def test_spending_by_category(transactions_before, transactions_after):
    result = spending_by_category(
        transactions=transactions_before, date="15.07.2018 16:49:53", category="Связь"
    )
    assert result == transactions_after.to_dict(orient="records")
