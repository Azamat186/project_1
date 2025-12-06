from masks import get_mask_card_number, get_mask_account
import re
from datetime import datetime


def get_date(iso_string: str) -> str:
    """Преобразование строки даты из формата ISO в формат ДД.ММ.ГГГГ."""
    try:
        dt_obj = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))
        return dt_obj.strftime("%d.%m.%Y")
    except ValueError as e:
        raise ValueError(f"Ошибка преобразования даты: {e}")


def mask_account_card(data: str) -> str:
    """Функция принимает строку с описанием карты или счета и номером, возвращает замаскированную версию."""
    pattern = r"^(?P<type>(карта|счет))\s+(?P<name>\S+)\s+(?P<number>\d+)$"
    match = re.match(pattern, data.strip())

    if not match:
        raise ValueError("Неправильный формат входных данных.")

    account_type = match.group("type")
    account_name = match.group("name")
    account_number = match.group("number")

    if account_type.lower() == "карта":
        return get_mask_card_number(int(account_number))
    elif account_type.lower() == "счет":
        return get_mask_account(account_number)
    else:
        raise ValueError("Тип учетной записи неизвестен.")


# Тестируем функции
try:
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Результат: 7000 79** **** 6361
    print(mask_account_card("Счет ВТБ Банк 73654108430135874305"))  # Результат: **4305
except Exception as ex:
    print(ex)
