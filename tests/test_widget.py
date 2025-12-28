import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("input_data, expected", [
    ("Visa Platinum 7000 79** **** 6361", "Visa Platinum 7000 79  6361"),
    ("Maestro 1596 83 **** 5199", "Maestro 1596 83  5199"),
    ("Счет **4305", "Счет **4305"),
    ("Visa Gold 5999 41 **** 6353", "Visa Gold 5999 41 ** 6353"),
])
def test_mask_account_card(input_data, expected):
    """Тестирует корректную работу функции mask_account_card
    с разными входными данными."""
    result = mask_account_card(input_data)
    print(f"Input: {input_data}, Expected: {expected}, Result: {result}")
    assert result == expected


@pytest.mark.parametrize("input_data", [
    "Visa Platinum 7000792289606361123123",
    "CrazyCard 123",
])
def test_mask_account_card_negative(input_data):
    """Опциональный тест на обработку некорректных данных"""
    try:
        mask_account_card(input_data)
    except Exception as e:
        pass
    else:
        raise AssertionError("Должна была быть выброшена ошибка!")


def test_mask_account_card_errors():
    """Тестирует выброс ошибок при некорректных данных."""
    with pytest.raises(ValueError, match="Некорректный ввод"):
        mask_account_card("Visa")
    with pytest.raises(ValueError, match="Некорректный номер карты/счета"):
        mask_account_card("Visa Platinum 1234asd56")


@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2019-07-03T18:35:29.512364", "03.07.2019"),
])
def test_get_date(date_str, expected):
    """Тестирует преобразование даты."""
    result = get_date(date_str)
    print(f"Input: {date_str}, Expected: {expected}, Result: {result}")
    assert result == expected
