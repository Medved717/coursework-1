import pytest

from unittest.mock import patch, Mock
from src.reports import get_transactions_in_excel_file, spending_by_category


@patch('src.reports.pd.read_excel')
@patch('src.reports.os.path.join')
def test_get_transactions_in_excel_file(mock_join, mock_read_excel, operations_dataframe):
    mock_join.return_value = 'Путь к файлу'
    mock_read_excel.return_value = operations_dataframe
    result = get_transactions_in_excel_file()
    assert result.to_dict() == operations_dataframe.to_dict()