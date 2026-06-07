from datetime import datetime


def get_result_list_transaction_by_date(transactions: list[dict], input_date: str) -> list[dict]:
    """Прием даты и формирование списка словарей
    с начала месяца по полученной дате в формате от меньшей даты к большей."""

    # Приводим введенную дату в объект datetime.
    datetime_input = datetime.strptime(input_date, '%d.%m.%Y %H:%M:%S')
    # Откатываем введенную дату на начало месяца.
    datetime_beginning_of_the_month = datetime_input.replace(day=1, hour=0, minute=0, second=0)

    # Формируем условие, при котором транзации формируются исходя из периода дат.
    list_transactions = []
    for transaction in transactions:
        transaction_obj_date = datetime.strptime(transaction['Дата операции'],'%d.%m.%Y %H:%M:%S')
        if datetime_beginning_of_the_month <= transaction_obj_date <= datetime_input:
            list_transactions.append(transaction)
    return sorted(list_transactions, key=lambda  x: x['Дата операции'],   reverse=False)
