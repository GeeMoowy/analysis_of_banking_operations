import json
from pathlib import Path

from src.main import time_of_day, get_cards_group_by_expenses
from src.utils import read_all_data


PATH_TO_ROOT = Path(__file__).parent.parent
PATH_TO_FILE = Path(PATH_TO_ROOT, 'data', 'operations.xlsx')


def main(date_time: str):
    df = read_all_data(PATH_TO_FILE)
    data = {
        "greeting": time_of_day(date_time),
        "cards": get_cards_group_by_expenses(df)
    }
    json_result = json.dumps(data, ensure_ascii=False, indent=4)
    return json_result


