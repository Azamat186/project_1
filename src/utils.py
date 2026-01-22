import json
from typing import Union, List, Dict


def read_json_file(file_path: str) -> Union[List[Dict], List]:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    Если файл не существует, пустой или содержит неправильные данные, возвращает пустой список.
    :param file_path: путь к файлу JSON
    :type file_path: str
    :rtype: list
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            transactions = json.load(f)

            # Проверяем, что данные представляют собой список
            if isinstance(transactions, list):
                return transactions
            else:
                print("Ошибка: Ожидается список транзакций")
                return []

    except FileNotFoundError:
        print("Ошибка: Файл не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка: Некорректный формат JSON")
        return []
