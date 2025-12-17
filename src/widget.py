from typing import Optional
from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(info_string: str) -> str:
    """
    Применяет соответствующую маску к номеру карты или счёта,
    указанным в строке info_string.

    :param info_string: Строка вида "<тип объекта> <номер>"
    Возможные значения: "Visa Platinum", "Maestro", "MasterCard", "Счёт"
    :return: Замасированное представление строки с типом и номером
    """
    parts = info_string.split()
    type_name = parts[0].strip()  # Тип (например, Visa Platinum или Счет)
    number_str = ''.join(parts[1:])

    try:
        number = int(number_str)
    except ValueError as e:
        raise ValueError(f"Ошибка парсинга номера '{number_str}'") from e

    # Ищем последний элемент, который полностью состоит из цифр
    for i in range(len(parts) - 1, -1, -1):
        if parts[i].isdigit():
            number_str = parts[i]
            type_name = " ".join(parts[:i])
            break
    else:
        raise ValueError(f"Не удалось найти числовой номер в строке '{info_string}'")

    # Преобразуем номер в int
    number = int(number_str)

    if type_name.lower().startswith('счет'):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{type_name} {masked_number}"

def get_date(date_time_str: str) -> str:
    """
    Преобразует строку с датой-временем в удобный формат ДД.ММ.ГГГГ.

    :param date_time_str: Исходная строка даты-времени ("2024-03-11T02:26:18.671407").
    :return: Форматированный результат ("11.03.2024").
    """
    dt_obj = datetime.fromisoformat(date_time_str[:-7])
    return dt_obj.strftime("%d.%m.%Y")
