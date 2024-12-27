from datetime import datetime
from pathlib import Path
from typing import Any
import pandas as pd


def time_of_day(my_datetime: str) -> str:
    """Функция принимает строку с датой и временем и возвращает строку с приветствием в текущем времени суток"""
    my_datetime_obj = datetime.strptime(my_datetime, "%Y-%m-%d %H:%M:%S")
    my_time = my_datetime_obj.time()  # Извлекаем время

    if my_time < datetime.strptime("04:00", "%H:%M").time():
        return "Доброй ночи"
    elif my_time < datetime.strptime("11:00", "%H:%M").time():
        return "Доброе утро"
    elif my_time < datetime.strptime("16:00", "%H:%M").time():
        return "Добрый день"
    else:
        return "Добрый вечер"


def get_cards_group_by_expenses(all_df: pd.DataFrame) -> list[dict[str, float | Any]]:
    """Функция принимает dataframe с тарнзакциями и возвращает сгруппированный и отфильтрованный словарь
     с маской номера карты, суммой расходов и кэшбеком по сумме расходов"""
    # Фильтруем строки, оставляя только расходы
    filtered_df = all_df.loc[all_df['Сумма операции'] < 0]

    cards_df = filtered_df.groupby(['Номер карты'])  # Группируем по номеру карты
    new_df = cards_df['Сумма операции'].sum()  # Суммируем операции

    result_list = []  # Создаем пустой список для результатов

    # Добавляем кэшбек и формируем список
    for card_number, total in new_df.items():
        result_list.append({
            "last_digits": card_number,
            "total_spent": total,
            "cashback": total / 100  # 1 руб. кэшбек на 100 руб.
        })

    return result_list
