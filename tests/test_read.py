import pytest
from unittest.mock import Mock, patch
from src.read_file import get_csv_stocks, get_transactions_excel


@patch('src.read_file.pd.read_excel')
@patch('src.read_file.os.path.join')
def test_get_transactions_excel(mock_os_path_join, mock_pd_read_excel):
    """Проверяем вывод списка словарей."""

    mock_os_path_join.return_value = 'Путь к файлу'
    mock_df = Mock()
    mock_pd_read_excel.return_value = mock_df
    mock_were = Mock()
    mock_df.where.return_value = mock_were
    mock_were.to_dict.return_value = [{'id': 1, 'name': 'test'}]
    result = get_transactions_excel()
    assert result == [{'id': 1, 'name': 'test'}]


@patch('src.read_file.pd.read_csv')
@patch('src.read_file.os.path.join')
def test_get_csv_stocks(mock_os_path_join, mock_pd_read_csv, stock_list_data, stock_list_filter):
    """Мокаем join и pd.read_csv, после чего выводим список словарей."""

    mock_os_path_join.return_value = 'Текст пути к файлу.'
    mock_result_read_csv = Mock()
    mock_pd_read_csv.return_value = mock_result_read_csv
    mock_result_read_csv.to_dict.return_value = stock_list_data
    result = get_csv_stocks()
    assert result == stock_list_filter


@patch('src.read_file.pd.read_csv')
@patch('src.read_file.os.path.join')
def test_get_csv_stocks_path(mock_join, mock_read, stock_list_data, stock_list_filter):
    """Тестирование использования csv файла и вывода необходимых словарей."""

    mock_join.return_value = 'Строка с путем к файлу.'
    fake_read_csv = Mock()
    mock_read.return_value = fake_read_csv
    fake_read_csv.to_dict.return_value = stock_list_data
    result = get_csv_stocks()
    assert result == stock_list_filter

