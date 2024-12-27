import pandas as pd


def categories_for_cashback(my_data, year, month):
    """Функция принимает данные для анализа, год и месяц и анализирует,
    сколько можно заработать кэшбека по каждой категории покупок"""
    my_data['Дата платежа'] = pd.to_datetime(my_data['Дата платежа'], format='%d.%m.%Y')
    filtered_data_by_date = my_data[(my_data['Дата платежа'].dt.month == month) &
                                    (my_data['Дата платежа'].dt.year == year)]
    expenses_data = filtered_data_by_date[filtered_data_by_date['Сумма операции'] < 0]
    cashback_by_category = expenses_data.groupby('Категория')['Сумма операции'].sum().abs()
    cashback_by_category = round((cashback_by_category / 100), 1).to_dict()

    return cashback_by_category


# data = read_all_data('C:/Users/USER/PycharmProjects/analysis_of_banking_operations/data/operations.xlsx')
# print(categories_for_cashback(data, 2019, 5))
