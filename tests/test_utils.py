from unittest.mock import patch
import pandas as pd
import pytest

from src.utils import read_excel


@pytest.fixture
def mocked_read_excel():
    with patch('src.utils.read_excel') as mocked_func:
        mocked_func.return_value = pd.DataFrame({
        "Дата операции": ["31.12.2021 16:44:00"],
        "Дата платежа": ["31.12.2021"],
        "Номер карты": ["*7197"],
        "Статус": ["OK"],
        "Сумма операции": [-160,89],
        "Валюта операции": ["RUB"],
        "Сумма платежа": [-837.9],
        "Валюта платежа": ["RUB"],
        "Кэшбэк": [1],
        "Категория": ["Супермаркеты"],
        "MCC": [5411],
        "Описание": ["Колхоз"],
        "Бонусы (включая кэшбэк)": [3.00],
        "Округление на инвесткопилку": [0.00],
        "Сумма операции с округлением": [160,89],
        })
    return mocked_func


def test_read_excel(mocked_read_excel):
    result = read_excel('C:/Users/USER/PycharmProjects/analysis_of_banking_operations/tests/test_operations.xlsx')

    expected_result = pd.DataFrame({
        "Дата операции": ["31.12.2021 16:44:00"],
        "Дата платежа": ["31.12.2021"],
        "Номер карты": ["*7197"],
        "Статус": ["OK"],
        "Сумма операции": [-160,89],
        "Валюта операции": ["RUB"],
        "Сумма платежа": [-837.9],
        "Валюта платежа": ["RUB"],
        "Кэшбэк": [1],
        "Категория": ["Супермаркеты"],
        "MCC": [5411],
        "Описание": ["Колхоз"],
        "Бонусы (включая кэшбэк)": [3.00],
        "Округление на инвесткопилку": [0.00],
        "Сумма операции с округлением": [160,89],
    })

    # Используем метод .equals() для сравнения DataFrame
    pd.testing.assert_frame_equal(result, expected_result)
