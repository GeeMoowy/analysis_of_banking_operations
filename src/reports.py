from datetime import datetime, timedelta
from typing import Optional
import pandas as pd

from src.utils import read_all_data


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    if date is None:
        date = datetime.now().strftime('%d.%m.%Y')
    end_date = datetime.strptime(date, '%d.%m.%Y')
    start_date = end_date - timedelta(days=90)
    transactions['Дата платежа'] = pd.to_datetime(transactions['Дата платежа'], format='%d.%m.%Y')
    filtered_transactions = transactions[
        (transactions['Категория'] == category) &
        (transactions['Дата платежа'] >= start_date) &
        (transactions['Дата платежа'] <= end_date)
        ]
    return filtered_transactions[['Дата платежа', 'Категория', 'Сумма платежа']]


# data = read_all_data('C:/Users/USER/PycharmProjects/analysis_of_banking_operations/data/operations.xlsx')
# print(spending_by_category(data, 'Аптеки', '12.10.2020'))