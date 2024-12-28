from pathlib import Path
from typing import Union
import pandas as pd
from pandas import DataFrame


PATH_TO_ROOT = Path(__file__).parent.parent
PATH_TO_DIR = Path(PATH_TO_ROOT, 'data')


def read_all_data(file_path: Union[str, Path]) -> DataFrame:
    """Функция принимает путь к excel файлу, читает и возвращает DataFrame объект"""
    all_data_df = pd.read_excel(file_path)
    return all_data_df


def reports_result(filename=None):
    """Внешняя функция, которая принимает аргумент filename для декоратора,
    для создания файла с результатами работы функции"""
    def inner(func):
        """Декоратор, принимает функцию для декорирования"""
        def wrapper(*args, **kwargs):
            """Функция обертка, которая принимает аргументы декорируемой функции"""
            res = func(*args, **kwargs)
            if filename:  # Проверка на наличие атрибута у filename
                path_to_file = Path(PATH_TO_DIR, filename)
                with open(path_to_file, "a", encoding="utf-8") as file:
                    file.write(f"Результат функции {func.__name__} =\n {res}\n")
            else:
                print(f"{func.__name__} OK\n")  # Выводим данные в консоль
            return res
        return wrapper
    return inner
