import datetime

import pytest
from unittest.mock import patch, MagicMock

from src.greeting import get_time, greeting_users


@patch('src.greeting.datetime')
def test_get_time(mock_datetime):
    """Тестирование методом mock по настоящему времени с подменой."""

    mock_datetime.now.return_value = datetime.datetime(2026, 6, 3, 10, 28, 4)
    result = get_time()
    assert result == '2026-06-03 10:28:04'


@patch('src.greeting.datetime')
def test_greeting_users_morning(mock_get_time):
    """Тест по выводу: 'Доброе утро'"""

    mock_get_time.return_value = '2026-06-03 10:28:04'
    result = greeting_users(mock_get_time.return_value)
    assert result == 'Доброе утро!'


@patch('src.greeting.datetime')
def test_greeting_users_day(mock_get_time):
    """Тест по выводу: 'Добрый день!'"""

    mock_get_time.return_value = '2026-06-03 15:28:04'
    result = greeting_users(mock_get_time.return_value)
    assert result == 'Добрый день!'


@patch('src.greeting.datetime')
def test_greeting_users_evening(mock_get_time):
    """Тест по выводу: 'Добрый вечер!'"""

    mock_get_time.return_value = '2026-06-03 20:28:04'
    result = greeting_users(mock_get_time.return_value)
    assert result == 'Добрый вечер!'


@patch('src.greeting.datetime')
def test_greeting_users_night(mock_get_time):
    """Тест по выводу: 'Доброй ночи!'"""

    mock_get_time.return_value = '2026-06-03 03:28:04'
    result = greeting_users(mock_get_time.return_value)
    assert result == 'Доброй ночи!'
