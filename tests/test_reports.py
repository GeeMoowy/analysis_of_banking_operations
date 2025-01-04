import pandas as pd
import json
from datetime import datetime, timedelta

from src.reports import spending_by_category


def test_spending_by_category(data):
    transactions = pd.DataFrame(data)
    transactions["Дата платежа"] = pd.to_datetime(transactions["Дата платежа"], format="%d.%m.%Y")
    category = "Супермаркеты"
    date = "25.01.2021"  # Тестируем на дату, которая входит в диапазон
    expected_result = json.dumps({"Супермаркеты": 350}, ensure_ascii=False, indent=4)
    result = spending_by_category(transactions, category, date)
    assert result == expected_result


def test_spending_by_category_with_none_date(data):
    transactions = pd.DataFrame(data)
    transactions["Дата платежа"] = pd.to_datetime(transactions["Дата платежа"], format="%d.%m.%Y")
    category = "Супермаркеты"
    current_date = datetime.now().strftime("%d.%m.%Y")
    expected_result = json.dumps({}, ensure_ascii=False, indent=4)
    # Вызываем функцию с date=None
    result = spending_by_category(transactions, category, None)
    assert result == expected_result