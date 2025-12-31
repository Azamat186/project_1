import pytest
from src.widget import mask_account_card, get_date
from datetime import datetime


def mask_account_card(info_string: str) -> str:
    # Проверяем, есть ли пробел между названием карты и номером
    if ' ' in info_string:
        parts = info_string.split()
        type_name = parts[0].strip()
        number_str = ''.join(parts[1:]).strip()
    else:
        # Если пробела нет, предполагаем, что название карты идет перед номером
        split_pos = len(info_string) - 16  # последние 16 символов — это номер
        type_name = info_string[:split_pos].strip()
        number_str = info_string[split_pos:].strip()

    # Маскируем номер карты
    if len(number_str) == 16:
        masked_number = f"{number_str[:6]} **** **** {number_str[-4:]}"
    elif len(number_str) == 4:  # если это счёт
        masked_number = f"**{number_str[-4:]}"
    else:
        raise ValueError("Некорректная длина номера карты")

    return f"{type_name} {masked_number}"

def get_date(date_str: str) -> str:
    dt = datetime.fromisoformat(date_str.replace("T", " "))
    return dt.strftime("%d.%m.%Y")

# Тесты
@pytest.mark.parametrize("input_data, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 7365410843014305", "Счет **4305"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
])

def test_mask_account_card(input_data, expected):
    """Тестирует корректную работу функции mask_account_card с разными входными данными."""
    result = mask_account_card(input_data)
    # Убираем лишние пробелы и сравниваем
    assert result.strip() == expected.strip()

@pytest.mark.parametrize("input_data", [
    "Visa Platinum 7000792289606361123123",  # Слишком длинный номер
    "CrazyCard 123",                          # Некорректный тип карты
])
def test_mask_account_card_negative(info_string: str) -> str:
    # Проверяем, есть ли пробел между названием карты и номером
    if ' ' in info_string:
        parts = info_string.split()
        type_name = parts[0].strip()
        number_str = ''.join(parts[1:]).strip()
    else:
        # Если пробела нет, предполагаем, что название карты идет перед номером
        split_pos = len(info_string) - 16  # последние 16 символов — это номер
        type_name = info_string[:split_pos].strip()
        number_str = info_string[split_pos:].strip()

    # Проверка на корректность данных
    if len(number_str) != 16 and len(number_str) != 4:
        raise ValueError("Некорректная длина номера карты")

    # Маскируем номер карты
    if len(number_str) == 16:
        masked_number = f"{number_str[:6]} **** **** {number_str[-4:]}"
    elif len(number_str) == 4:  # если это счёт
        masked_number = f"**{number_str[-4:]}"

    return f"{type_name} {masked_number}"

@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2019-07-03T18:35:29.512364", "03.07.2019"),
])
def test_get_date(date_str, expected):
    """Тестирует преобразование даты."""
    assert get_date(date_str) == expected
