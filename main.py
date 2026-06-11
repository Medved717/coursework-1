from src.views import get_time, greeting_users, get_result_list_transaction_by_date, get_transactions_excel, mask_card, \
    cashback, total_expenses, payment_amount

# Получаем время обращения к программе.
get_time = get_time()

# Приветствуем пользователя в зависимости от времени.
print(greeting_users(get_time))

# Получаем список транзакций из файла.
transactions = get_transactions_excel()

# Маскируем номера карт в транзакциях (в данном случае убираем звездочки и оставляем просто 4 цифры).
transactions = mask_card(transactions)

# Подсчитываем кэшбек
transactions = cashback(transactions)

print('Программа: Хотите ли вы получить список транзакций с начала месяца и по интересующую дату?')

while True:
    get_date = input('Программа: Введите ответ: да или нет.').lower()
    if get_date == 'да':
        # Просим пользователя ввести дату, и получаем список транзакций с начала месяца.
        get_date_and_time = input('Введите дату и время в формате ДД.ММ.ГГГГ ЧЧ:MM:CC.')
        list_transaction_start_month = get_result_list_transaction_by_date(transactions, get_date_and_time)
        print(f'Получены сведения о транзакциях  с начала месяца.')
        print(list_transaction_start_month)
        break
    elif get_date == 'нет':
        list_transaction_start_month = transactions
        break

print('Хотите получить общую сумму расходов или доходов за указанный период?')

while True:
    get_ansver = input('Да или нет?').lower()
    if get_ansver == 'да':
        transactions_expenses = total_expenses(list_transaction_start_month)
    elif get_ansver == 'нет':
        break


# """Ведется подсчет топ-5 транзакций по сумме платежа (от самых больших и в обратном порядке)."""
print('Программа: Хотите получить подсчет топ-5 транзакций по сумме платежа (от самых больших и в обратном порядке)?')

while True:
    input_answer = input('Да или нет?').lower()
    if input_answer == 'да':
        result_payment_amount = payment_amount(list_transaction_start_month)
        break
    elif input_answer == 'нет':
        break

