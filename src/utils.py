from pathlib import Path
from typing import Union
import pandas as pd
from pandas import DataFrame


def read_all_data(file_path: Union[str, Path]) -> DataFrame:
    """Функция принимает путь к excel файлу, читает и возвращает DataFrame объект"""
    all_data_df = pd.read_excel(file_path)
    return all_data_df

