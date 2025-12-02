from typing import Union
import re
from datetime import datetime


def get_mask_card_number(card_number: int) -> str:
    """Получает число с номером кредитной карты и формирует её маску вида XXXX XX** **** XXXX."""
    card_str = str(card_number)
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Неверный формат номера карты")

    # Маска для первой части номера карты
    first_part = card_str[:4]
    second_part = card_str[4:6]
    third_part = "**"
    fourth_part = "**"
    fifth_part = card_str[-4:]

    return f"{first_part} {second_part}{third_part} {fourth_part} {fifth_part}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Формирует маску банковского счёта вида **XXXX."""
    acc_str = str(account_number)
    if len(acc_str) < 4 or not acc_str.isdigit():
        raise ValueError("Неверный формат номера счёта")

    last_four_digits = acc_str[-4:]
    return f"**{last_four_digits}"


# Функциональность преобразования даты
def get_date(iso_string: str) -> str:
    """Преобразование строки даты из формата ISO в формат ДД.ММ.ГГГГ."""
    try:
        dt_obj = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))
        return dt_obj.strftime("%d.%m.%Y")
    except ValueError as e:
        raise ValueError(f"Ошибка преобразования даты: {e}")


def mask_account_card(data: str) -> str:
    """Функция принимает строку с типом ('карта' или 'счет') и номером,
    возвращает замаскированный номер карты/счета."""
    match = re.match(r"^(карта|счет)\s+(\w+)$", data.strip())
    if not match:
        raise ValueError("Неправильный формат входных данных.")

    account_type, number = match.groups()

    if account_type.lower() == "карта":
        return get_mask_card_number(int(number))
    elif account_type.lower() == "счет":
        return get_mask_account(number)
    else:
        raise ValueError("Тип учетной записи неизвестен.")


# Тестируем функции
try:
    print(mask_account_card("карта 1234567890123456"))  # Результат: 1234 56** **** 3456
    print(mask_account_card("счет 123456789012"))  # Результат: **1234
except Exception as ex:
    print(ex)
