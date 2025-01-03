import json
from datetime import datetime, timedelta
from typing import Optional

import pandas as pd

from src.utils import read_excel, reports_result


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None):
    """Функция принимает датафрэйм, категорию покупки и дату
    и возвращает все покупки по данной категории за последние три месяца"""
    if date is None:
        date = datetime.now().strftime("%d.%m.%Y")
    end_date = datetime.strptime(date, "%d.%m.%Y")
    start_date = end_date - timedelta(days=90)
    transactions["Дата платежа"] = pd.to_datetime(transactions["Дата платежа"], format="%d.%m.%Y")
    filtered_transactions = transactions[
        (transactions["Категория"] == category)
        & (transactions["Дата платежа"] >= start_date)
        & (transactions["Дата платежа"] <= end_date)
    ]
    res = filtered_transactions.groupby("Категория")["Сумма платежа"].sum().abs()
    res_dict = res.to_dict()
    json_answer = json.dumps(res_dict, ensure_ascii=False, indent=4)
    return json_answer


if __name__ == "__main__":
    data = read_excel('C:/Users/USER/PycharmProjects/analysis_of_banking_operations/data/operations.xlsx')
    print(spending_by_category(data, 'Фастфуд', '12.10.2021'))
