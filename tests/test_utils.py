from datetime import datetime, time
from pathlib import Path

import pandas as pd
from unittest.mock import patch, mock_open
import pytest
from src.utils import read_excel, time_of_day, reports_result


def test_read_excel(data):
    expected_df = pd.DataFrame(data)
    with patch('pandas.read_excel', return_value=expected_df) as mock_read_excel:
        # Вызываем функцию
        result_df = read_excel("example.xlsx")
        # Проверяем, что pd.read_excel был вызван с правильным аргументом
        mock_read_excel.assert_called_once_with("example.xlsx")
        # Проверяем, что результат соответствует ожидаемому DataFrame
        pd.testing.assert_frame_equal(result_df, expected_df)


@pytest.mark.parametrize("date, expected", [("2021-10-12 15:13:10", "Добрый день"),
                                            ("2021-10-12 02:25:30", "Доброй ночи"),
                                            ("2021-10-12 10:20:20", "Доброе утро"),
                                            ("2021-10-12 20:58:16", "Добрый вечер")
                                            ]
                         )
def test_time_of_day(date, expected):
    assert time_of_day(date) == expected


@reports_result("test_results.txt")
def sample_function(x, y):
    return x + y

def test_reports_result_with_file():
    # Используем mock_open для имитации открытия файла
    m = mock_open()
    with patch("builtins.open", m):
        result = sample_function(3, 4)  # Вызываем декорированную функцию

        # Получаем полный путь к файлу
        expected_path = Path("C:/Users/USER/PycharmProjects/analysis_of_banking_operations/data/test_results.txt")

        # Проверяем, что файл открывается с правильными параметрами
        m.assert_called_once_with(expected_path, "a", encoding="utf-8")

        # Проверяем, что метод write был вызван с правильным аргументом
        m().write.assert_called_once_with("Результат функции sample_function =\n 7\n")

        # Проверяем, что результат функции правильный
        assert result == 7