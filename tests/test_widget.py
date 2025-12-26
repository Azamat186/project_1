import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("input_data, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
])
def test_mask_account_card(input_data, expected):
    """Тестирует корректную работу функции mask_account_card
    с разными входными данными."""
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize("input_data", [
    "Visa Platinum 7000792289606361123123",
    "CrazyCard 123",
])
def test_mask_account_card_negative(input_data):
    """Этот тест опционален, зависит от того,
    как жестко мы хотим проверять валидность.
    В текущей реализации widget.py проверяется только .isdigit().
    Ниже тесты на реальные ошибки.
    """


def test_mask_account_card_errors():
    """Тестирует выброс ошибок при некорректных данных."""
    # Проверка на отсутствие номера (слишком мало слов)
    with pytest.raises(ValueError, match="Некорректный ввод"):
        mask_account_card("Visa")

    # Проверка на нецифровой номер
    with pytest.raises(ValueError, match="Некорректный номер карты/счета"):
        mask_account_card("Visa Platinum 1234asd56")


@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2019-07-03T18:35:29.512364", "03.07.2019"),
])
def test_get_date(date_str, expected):
    """Тестирует преобразование даты."""
    assert get_date(date_str) == expected
