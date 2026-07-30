from src.reports import get_transactions_in_excel_file, spending_by_category
from src.services import (get_analysis_increased_cashback,
                          get_categories_cashback)
from src.views import (cashback, file_csv_stocks, get_csv_stocks,
                       get_exchange_rate, get_result_list_transaction_by_date,
                       get_stocks, get_time, get_transactions_excel,
                       greeting_users, mask_card, payment_amount,
                       total_expenses, get_currencies_and_stocks, save_currencies_and_stocks)

if __name__ == "__main__":

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

    print(
        "Программа: Хотите ли вы получить список транзакций с начала месяца и по интересующую дату?"
    )

    while True:
        get_date = input("Программа: Введите ответ: да или нет.").lower()
        if get_date == "да":
            # Просим пользователя ввести дату, и получаем список транзакций с начала месяца.
            get_date_and_time = input(
                "Введите дату и время в формате ДД.ММ.ГГГГ ЧЧ:MM:CC."
            )
            list_transaction_start_month = get_result_list_transaction_by_date(
                transactions, get_date_and_time
            )
            print("Получены сведения о транзакциях  с начала месяца.")
            break
        elif get_date == "нет":
            list_transaction_start_month = None
            break

    # Gолучаем транзакции с учетом кэшбека за 3 месяца.
    print("Программа: Хотите получить транзакции с учетом кэшбека за 3 месяца?")
    while True:
        input_answer = input("Программа: Введите ответ: да или нет.").lower()
        if input_answer == "да":
            while True:
                input_month = input('Программа: Введите месяц в формете "ММ".')
                break
            while True:
                input_year = input('Программа: Введите год в формете "YYYY".')
                break
            analysis_cashback = get_analysis_increased_cashback(
                transactions, str(input_month), str(input_year)
            )
            result_cashback = get_categories_cashback(analysis_cashback)
            break
        elif input_answer == "да":
            analysis_cashback = None

    # Получаем сведения по общим расходам за период.
    print("Хотите получить общую сумму расходов или доходов за указанный период?")
    while True:
        get_ansver = input("Программа: Введите ответ: да или нет.").lower()
        if get_ansver == "да":
            transactions_expenses = total_expenses(list_transaction_start_month)
            print("Получены сведения об общей сумме расходов.")
            break
        elif get_ansver == "нет":
            transactions_expenses = None
            break

    # """Ведется подсчет топ-5 транзакций по сумме платежа (от самых больших и в обратном порядке)."""
    print(
        "Программа: Хотите получить подсчет топ-5 транзакций по сумме платежа (от самых больших и в обратном порядке)?"
    )

    while True:
        input_answer = input("Программа: Введите ответ: да или нет.").lower()
        if input_answer == "да":
            result_payment_amount = payment_amount(list_transaction_start_month)
            print("Получены сведения о топ-5 транзакций по сумме платежа.")
            break
        elif input_answer == "нет":
            result_payment_amount = None
            break

    # Получаем сведения об акциях.
    print("Программа: Получить сведения об акциях?")
    while True:
        input_answer = input("Программа: Введите ответ: да или нет.").lower()
        if input_answer == "да":
            get_stocks()
            list_stocks = get_csv_stocks()
            print("Получены сведения о стоимости акций.")
            print("Программа: Сохранить полученные сведения в csv - файл?")
            while True:
                input_answer = input("Да или нет?").lower()
                if input_answer == "да":
                    file_csv_stocks()
                    print("Сведения сохранены в csv - файл.")
                    break
                elif input_answer == "нет":
                    break
            break
        elif input_answer == "нет":
            list_stocks = None
            break

    # Получаем сведения о курсе валют.
    print("Программа: Получить данные о курсе валют?")
    while True:
        input_answer = input("Программа: Введите ответ: да или нет.").lower()
        if input_answer == "да":
            exchange_rate = get_exchange_rate()
            print("Получены сведения о курсе валют.")
            break
        elif input_answer == "нет":
            exchange_rate = None
            break

    # Получаем сведения о курсе валют и акциях.
    print("Программа: Сохранить данные об акциях и курсу валют в json-файл?")
    while True:
        input_answer = input("Программа: Введите ответ: да или нет.").lower()
        if input_answer == "да":
            dict_currencies_and_stocks = get_currencies_and_stocks(get_csv_stocks(), get_exchange_rate())
            save_currencies_and_stocks(dict_currencies_and_stocks)
            print("Данные о курсе валют и акциях сохранены!")
            break
        elif input_answer == "нет":
            exchange_rate = None
            break

    # Получаем список транзакций и выводим сведения о тратах по категориям за последние 3 месяца.
    print(
        "Программа: Желаете получить сведения о тратах по категории за последние 3 месяца?"
    )
    while True:
        input_result = input("Программа: Введите ответ: да или нет.").lower()
        if input_result == "да":
            transactions_excel = get_transactions_in_excel_file()
            while True:
                input_result_category = input(
                    "Программа: Введите искомую категорию c заглавной буквы."
                )
                category = str(input_result_category)
                break
            while True:
                input_result_date = input(
                    "Программа: Введите искомую дату в формате ДД.ММ.ГГГГ ЧЧ:MM:CC."
                )
                date = str(input_result_date)
                break
            get_spending_by_category = spending_by_category(
                transactions_excel, category, date
            )
            break
        elif input_answer == "нет":
            get_spending_by_category = None
            break

    # Выводим результаты модуля views.
    print(
        f"Получены следующие сведения.\n"
        f" Список транзакций с начала искомого месяца: \n"
        f"{list_transaction_start_month} \n"
        f"Кэшбек за 3 месяца:\n"
        f"{result_cashback}\n"
        f"Сумма прибыли / расходов: \n"
        f"{transactions_expenses}\n"
        f"Топ-5 транзакций по сумме платежа:\n"
        f"{result_payment_amount} \n"
        f"Сведения об акциях \n"
        f"{list_stocks}."
    )

    if get_spending_by_category:
        print(f"Расходы по категории за 3 месяца:\n" f"{get_spending_by_category}")
    else:
        print(
            "Расходы по категории за 3 месяца:\n"
            "Данная категория отсутствует в указанном периоде!"
        )
