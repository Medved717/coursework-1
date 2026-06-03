import datetime

import pytest
from unittest.mock import patch, MagicMock

from src.views import get_time, greeting


@patch('src.views.datetime')
def test_get_time(mock_datetime):
    """Тестирование методом mock по настоящему времени с подменой."""

    mock_datetime.now.return_value = datetime.datetime(2026, 6, 3, 10, 28, 4)
    result = get_time()
    assert result == '2026-06-03 10:28:04'


@patch('src.views.get_time')
def test_greeting_morning(mock_get_time):
    """Тест по выводу: 'Доброе утро'"""

    mock_get_time.return_value = '2026-06-03 10:28:04'
    result = greeting(mock_get_time.return_value)
    assert result == 'Доброе утро!'


@patch('src.views.get_time')
def test_greeting_day(mock_get_time):
    """Тест по выводу: 'Добрый день!'"""

    mock_get_time.return_value = '2026-06-03 15:28:04'
    result = greeting(mock_get_time.return_value)
    assert result == 'Добрый день!'


@patch('src.views.get_time')
def test_greeting_evening(mock_get_time):
    """Тест по выводу: 'Добрый вечер!'"""

    mock_get_time.return_value = '2026-06-03 20:28:04'
    result = greeting(mock_get_time.return_value)
    assert result == 'Добрый вечер!'


@patch('src.views.get_time')
def test_greeting_night(mock_get_time):
    """Тест по выводу: 'Доброй ночи!'"""

    mock_get_time.return_value = '2026-06-03 03:28:04'
    result = greeting(mock_get_time.return_value)
    assert result == 'Доброй ночи!'

