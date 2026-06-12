from src.services import get_analysis_increased_cashback
from src.views import get_time, greeting_users, get_result_list_transaction_by_date, get_transactions_excel, mask_card, \
    cashback, total_expenses, payment_amount, get_csv_stocks, get_stocks, get_exchange_rate, file_csv_stocks

if __name__ == '__main__':

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
            break
        elif get_date == 'нет':
            list_transaction_start_month = None
            break












    # Прописать еще вторую функцию из модуля cervices!!!!!!!!!!!


    # print('Программа: Хотите получить транзакции с учетом кэшбека за 3 месяца?')
    # while True:
    #     input_answеr = input('Программа: Введите ответ: да или нет.').lower()
    #     if input_answеr == 'да':
    #         while True:
    #             input_month = input('Программа: Введите месяц в формете "ММ".')
    #             break
    #         while True:
    #             input_year = input('Программа: Введите год в формете "YYYY".')
    #             break
    #         analysis_cashback = get_analysis_increased_cashback(transactions, str(input_month), str(input_year))
    #         break
    #     elif input_answеr == 'да':
    #         analysis_cashback = None














    print('Хотите получить общую сумму расходов или доходов за указанный период?')
    while True:
        get_ansver = input('Программа: Введите ответ: да или нет.').lower()
        if get_ansver == 'да':
            transactions_expenses = total_expenses(list_transaction_start_month)
            print(f'Получены сведения об общей сумме расходов.')
            break
        elif get_ansver == 'нет':
            transactions_expenses = None
            break


    # """Ведется подсчет топ-5 транзакций по сумме платежа (от самых больших и в обратном порядке)."""
    print('Программа: Хотите получить подсчет топ-5 транзакций по сумме платежа (от самых больших и в обратном порядке)?')

    while True:
        input_answer = input('Программа: Введите ответ: да или нет.').lower()
        if input_answer == 'да':
            result_payment_amount = payment_amount(list_transaction_start_month)
            print(f'Получены сведения о топ-5 транзакций по сумме платежа.')
            break
        elif input_answer == 'нет':
            result_payment_amount = None
            break


    # Получаем сведения об акциях.
    print('Программа: Получить сведения об акциях?')
    while True:
        input_answer = input('Программа: Введите ответ: да или нет.').lower()
        if input_answer == 'да':
            get_stocks()
            list_stocks = get_csv_stocks()
            print(f'Получены сведения о стоимости акций.')
            print('Программа: Сохранить полученные сведения в csv - файл?')
            while True:
                input_answer = input('Да или нет?').lower()
                if input_answer == 'да':
                    file_csv_stocks()
                    print(f'Сведения сохранены в csv - файл.')
                    break
                elif input_answer == 'нет':
                    break
            break
        elif input_answer == 'нет':
            list_stocks = None
            break


    # Получаем сведения о курсе валют.
    print('Программа: Получить данные о курсе валют?')
    while True:
        input_answer = input('Программа: Введите ответ: да или нет.').lower()
        if input_answer == 'да':
            exchange_rate = get_exchange_rate()
            print(f'Получены сведения о курсе валют.')
            break
        elif input_answer == 'нет':
            exchange_rate = None
            break

# Выводим результаты модуля views.
print(f'Получены следующие сведения.\n'
      f' Список транзакций с начала искомого месяца: \n'
      f'{list_transaction_start_month} \n'
      # f'Транзакции за 3 месяца:\n'
      # f'{analysis_cashback}\n'
      f'Сумма прибыли / расходов: \n'
      f'{transactions_expenses}\n'
      f'Топ-5 транзакций по сумме платежа:\n'
      f'{result_payment_amount} \n'
      f'Сведения об акциях \n'
      f'{list_stocks}.')
