import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234****3456"),
        ("123456789012345", ValueError("Неверный формат номера карты")),
        ("abc123", ValueError("Неверный формат номера карты")),
    ],
)
def test_get_mask_card_number(card_number, expected):
    if isinstance(expected, Exception):
        with pytest.raises(type(expected)) as excinfo:
            get_mask_card_number(card_number)
        assert str(excinfo.value) == str(expected)
    else:
        result = get_mask_card_number(card_number)
        assert result == expected

@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("123456789012", "****12"),
        ("12345678901", ValueError("Неверный формат номера счета")),
        ("abc123", ValueError("Неверный формат номера счета")),
    ],
)
def test_get_mask_account(account_number, expected):
    if isinstance(expected, Exception):
        with pytest.raises(type(expected)) as excinfo:
            get_mask_account(account_number)
        assert str(excinfo.value) == str(expected)
    else:
        result = get_mask_account(account_number)
        assert result == expected
