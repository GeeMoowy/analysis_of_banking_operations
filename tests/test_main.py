import pytest
from unittest.mock import patch, MagicMock
from src.main import main
from src.services import categories_for_cashback
from unittest.mock import patch
from src.utils import read_excel


def test_main():
    # Путь к тестовому файлу
    test_file_path = "C:/Users/USER/PycharmProjects/analysis_of_banking_operations/tests/test_operations.xlsx"  # Убедитесь, что файл существует по этому пути
    test_date = "2021-12-10 10:44:39"
    with (patch('src.utils.read_excel', side_effect=lambda path: read_excel(path) if path == test_file_path else None),
          patch('builtins.input', side_effect=["1"]),
          patch('src.views.json_answer_web',
                return_value='{\n'
 '    "greeting": "Доброе утро",\n'
 '    "cards": [\n'
 '        {\n'
 '            "last_digits": "*5091",\n'
 '            "total_spent": 564.0,\n'
 '            "cashback": 5.64\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*7197",\n'
 '            "total_spent": 78.05,\n'
 '            "cashback": 0.7805\n'
 '        }\n'
 '    ]\n'
 '}'),
          patch('src.services.categories_for_cashback'),
          patch('src.reports.spending_by_category')):
        result = main(test_file_path, test_date)
        assert result == ('{\n'
 '    "greeting": "Доброе утро",\n'
 '    "cards": [\n'
 '        {\n'
 '            "last_digits": "*5091",\n'
 '            "total_spent": 564.0,\n'
 '            "cashback": 5.64\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*7197",\n'
 '            "total_spent": 78.05,\n'
 '            "cashback": 0.7805\n'
 '        }\n'
 '    ]\n'
 '}')


def test_main_services():
    # Путь к тестовому файлу
    test_file_path = "C:/Users/USER/PycharmProjects/analysis_of_banking_operations/tests/test_operations.xlsx"  # Убедитесь, что файл существует по этому пути
    test_date = "2021-12-10 10:44:39"
    with (patch('src.utils.read_excel', side_effect=lambda path: read_excel(path) if path == test_file_path else None),
          patch('builtins.input', side_effect=["2"]),
          patch('src.views.json_answer_web'),
          patch('src.services.categories_for_cashback',
                return_value='{\n    "Различные товары": 5.6,\n    "Супермаркеты": 0.8\n}'),
          patch('src.reports.spending_by_category')):
        result = main(test_file_path, test_date)
        assert result == '{\n    "Различные товары": 5.6,\n    "Супермаркеты": 0.8\n}'


def test_main_reports():
    # Путь к тестовому файлу
    test_file_path = "C:/Users/USER/PycharmProjects/analysis_of_banking_operations/tests/test_operations.xlsx"  # Убедитесь, что файл существует по этому пути
    test_date = "2021-12-10 10:44:39"
    with (patch('src.utils.read_excel', side_effect=lambda path: read_excel(path) if path == test_file_path else None),
          patch('builtins.input', side_effect=["3", "Супермаркеты", "31.12.2021"]),
          patch('src.views.json_answer_web'),
          patch('src.services.categories_for_cashback'),
          patch('src.reports.spending_by_category', return_value='{\n    "Супермаркеты": 78.05\n}')):
        result = main(test_file_path, test_date)
        assert result == '{\n    "Супермаркеты": 78.05\n}'