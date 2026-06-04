from datetime import datetime


def get_time():
    """Принимает время на момент использования и
    в зависимости от времени приветствует пользователя."""

    datetime_now = datetime.now()
    data_str = datetime_now.strftime('%Y-%m-%d %H:%M:%S')
    return data_str


def greeting_users(date: str) -> str:
    """Приветствие в зависимости от времени обращения."""

    if 5 <= int(date[11:13]) <= 11:
        return f'Доброе утро!'
    elif 12 <= int(date[11:13]) <= 15:
        return f'Добрый день!'
    elif 16 <= int(date[11:13]) <= 21:
        return f'Добрый вечер!'
    else:
        return f'Доброй ночи!'