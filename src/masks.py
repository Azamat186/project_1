def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску банковской карты вида XXXX XX** **** XXXX"""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Неверный формат номера карты")

    return f"{card_number[:4]} {card_number[4:6]} **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Возвращает маску аккаунта вида **XXXX"""
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Неверный формат номера счета")

    return f"{account_number[-4:]}"
